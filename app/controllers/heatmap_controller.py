import json
from pathlib import Path

import cv2
import numpy as np
import pandas as pd
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QImage
from scipy.ndimage import gaussian_filter

from app.ui.dialogs import SaveImgaeDialog
from app.utils import ColormapManager


class HeatmapController(QObject):
    def __init__(self, widget_ui, heatmap_configure, data_path, save_path):
        super().__init__()
        self.widget_ui = widget_ui
        self.folders = []
        self.data = pd.DataFrame(
            {
                "name": pd.Series(dtype="object"),
                "coords_x": pd.Series(dtype="object"),
                "coords_y": pd.Series(dtype="object"),
                "width": pd.Series(dtype="object"),
                "height": pd.Series(dtype="object"),
                "center_x": pd.Series(dtype="float64"),
                "center_y": pd.Series(dtype="float64"),
                "pixel_size": pd.Series(dtype="float64"),
                "mode": pd.Series(dtype="object"),
                "fps": pd.Series(dtype="float64"),
                "p": pd.Series(dtype="object"),
                "areaInt": pd.Series(dtype="float64"),
            }
        )
        self.FILTER_CONFIG = {
            0: {"query": None, "platform_allowed": False},
            1: {"query": "mode == 'box'", "platform_allowed": True},
            2: {"query": "mode == 'cross'", "platform_allowed": False},
            3: {"query": "mode == 'morris'", "platform_allowed": True},
            4: {"query": "mode == 'ldt'", "platform_allowed": False},
            5: {"query": "mode == 'ymt'", "platform_allowed": True},
            6: {"query": "mode == 'tcs'", "platform_allowed": True},
        }

        self.data_path = data_path
        self.widget_ui.setup_dialog_dir(data_path)
        self.save_path = save_path

        self.colormap_manager = ColormapManager()
        self.heatmap_configure = heatmap_configure
        self.apply_state_to_ui(self.heatmap_configure)
        self._setup_signals()

    def _setup_signals(self):
        self.widget_ui.add_folder_clicked.connect(self.on_add_folder)
        self.widget_ui.remove_folder_clicked.connect(self.on_remove_last_folder)
        self.widget_ui.clear_folders_clicked.connect(self.on_clear_folders)
        self.widget_ui.build_graph_clicked.connect(self.on_start)
        self.widget_ui.save_image_clicked.connect(self.on_save_image)

    def apply_state_to_ui(self, cfg):
        self.widget_ui.ui.dsbBoxScale.setValue(cfg.box_scale)
        self.widget_ui.ui.sbGausSigma.setValue(cfg.gaussian_sigma)
        self.widget_ui.ui.dsbZoom.setValue(cfg.zoom)
        self.widget_ui.ui.dsbGamma.setValue(cfg.gamma)
        self.widget_ui.ui.dsbAlpha.setValue(cfg.alpha)
        self.widget_ui.ui.dsbContrast.setValue(cfg.contrast)
        self.widget_ui.ui.cbAddColorbar.setChecked(cfg.is_add_colorbar)
        self.widget_ui.ui.chbAddPlatform.setChecked(cfg.platform_allowed)
        self.widget_ui.ui.chbMarkup.setChecked(cfg.markup)
        self.widget_ui.ui.chbOverlaps.setChecked(cfg.overlaps)
        self.widget_ui.ui.cbInterpolate.setChecked(cfg.interpolate)

    def on_add_folder(self, folders: list[str]):
        for folder_str in folders:
            folder = Path(folder_str)

            if not folder.exists():
                self.widget_ui.show_error(f"Folder {folder} does not exist")
                continue

            if folder in self.folders:
                self.widget_ui.show_warning(f"Folder {folder} is already added")
                continue

            is_ok = self._load_data(folder)
            if is_ok:
                self.folders.append(folder)
                self.widget_ui.add_folder_in_list(folder)

    def on_remove_last_folder(self):
        if not self.folders:
            self.widget_ui.show_error("No folders to remove")
            return

        folder = self.folders.pop()
        self.widget_ui.remove_last_folder()
        name = folder.name.split("_")[0]
        self.data = self.data[self.data["name"] != name]

    def on_clear_folders(self):
        self.folders.clear()
        self.widget_ui.clear_folders()

    def _load_data(self, folder_path: Path) -> bool:
        name = folder_path.name.split("_")[0]

        data_name = name + "_data.csv"
        print(f"DEBUG: data_name = {data_name}")
        if not (folder_path / data_name).exists():
            self.widget_ui.show_warning(
                f"The file with data {data_name} is missing from the directory {folder_path}. \nThe folder has not been added!"
            )
            return False

        cfg_name = name + "_cfg.json"
        print(f"DEBUG: cfg_name = {cfg_name}")
        if not (folder_path / cfg_name).exists():
            self.widget_ui.show_warning(
                f"The file with configuration {cfg_name} is missing from the directory {folder_path}. \nThe folder has not been added!"
            )
            return False

        df = pd.read_csv(folder_path / data_name)
        with open(folder_path / cfg_name) as f:
            metadata = json.load(f)
        # print(f"DEBUG: metadata = {metadata}")

        data = pd.DataFrame(
            [
                {
                    "name": name,
                    "coords_x": df["xc"].tolist(),
                    "coords_y": df["yc"].tolist(),
                    "width": df["width"].tolist(),
                    "height": df["height"].tolist(),
                    "center_x": metadata["p_center"][0],
                    "center_y": metadata["p_center"][1],
                    "pixel_size": metadata["pixel_size"],
                    "fps": metadata["fps"],
                    "mode": metadata.get("mode"),
                    "p": metadata.get("p", None),
                    "areaInt": metadata.get("areaInt", 0),
                }
            ],
        )
        print(f"DEBUG: data = {data}")
        self.data = pd.concat([self.data, data], ignore_index=True)

        return True

    def on_start(self):
        if len(self.folders) * len(self.data) == 0:
            self.widget_ui.show_error(
                "No data available to build the heatmap!"
            )
            return

        settings = self.widget_ui.collect_settings()

        filter = self.FILTER_CONFIG.get(settings["filter"], 0)
        if filter:
            if not filter["platform_allowed"] and settings["platform_allowed"]:
                self.widget_ui.clear_image()
                self.widget_ui.show_warning(
                    "For this filter, uncheck the 'Display Platform' checkbox"
                )
                return
            data = (
                self.data
                if filter["query"] is None
                else self.data.query(filter["query"])
            )
        else:
            data = self.data

        if len(data) == 0:
            self.widget_ui.clear_image()
            self.widget_ui.show_warning("No data available for the selected filter")
            return

        self.build_heatmap(settings, data)

    def build_heatmap(self, params, data):
        SIZE_PX = 3000
        GRID_SIZE = 3
        resolution = 20 * params["zoom"]
        center_shift_cm = SIZE_PX / (2 * resolution)

        if params["markup"]:
            block_height = SIZE_PX // GRID_SIZE
            block_width = SIZE_PX // GRID_SIZE
            time_matrix = np.zeros((GRID_SIZE, GRID_SIZE))
        else:
            time_matrix = None

        heatmaps_list = []
        # print(f"DEBUG: data = {data}")
        for _, row in data.iterrows():
            if params["interpolate"]:
                row["coords_x"] = (
                    pd.Series(row["coords_x"])
                    .replace(0, np.nan)
                    .interpolate()
                    .ffill()
                    .bfill()
                    .tolist()
                )
                row["coords_y"] = (
                    pd.Series(row["coords_y"])
                    .replace(0, np.nan)
                    .interpolate()
                    .ffill()
                    .bfill()
                    .tolist()
                )

            dx = center_shift_cm - row["center_x"] * row["pixel_size"]
            dy = center_shift_cm - row["center_y"] * row["pixel_size"]
            fps = row.get("fps", 1)

            all_points = []
            print(f"DEBUG: row = {row}")
            for x, y, w, h in zip(
                row["coords_x"], row["coords_y"], row["width"], row["height"]
            ):
                if x == 0 and y == 0:
                    continue

                x_cm = x * row["pixel_size"] + dx
                y_cm = y * row["pixel_size"] + dy
                w_cm = w * row["pixel_size"] // params["box_scale"]
                h_cm = h * row["pixel_size"] // params["box_scale"]

                x1 = int((x_cm - w_cm / 2) * resolution)
                y1 = int((y_cm - h_cm / 2) * resolution)
                x2 = int((x_cm + w_cm / 2) * resolution)
                y2 = int((y_cm + h_cm / 2) * resolution)

                x1 = max(0, min(SIZE_PX - 1, x1))
                y1 = max(0, min(SIZE_PX - 1, y1))
                x2 = max(0, min(SIZE_PX - 1, x2))
                y2 = max(0, min(SIZE_PX - 1, y2))

                if params["markup"]:
                    self.update_time_matrix(
                        time_matrix,
                        (x1, y1, x2, y2),
                        fps,
                        block_height,
                        block_width,
                        GRID_SIZE,
                        SIZE_PX,
                    )

                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                all_points.append((center_x, center_y))

            if all_points:
                all_points = np.array(all_points)

                heatmap = np.histogram2d(
                    all_points[:, 0],
                    all_points[:, 1],
                    bins=[SIZE_PX, SIZE_PX],
                    range=[[0, SIZE_PX], [0, SIZE_PX]],
                )[0].T
                heatmap = gaussian_filter(heatmap, sigma=params["gaussian_sigma"])
                heatmaps_list.append(heatmap)

        if not heatmaps_list:
            self.widget_ui.show_error("No valid data!")
            return

        if params.get("overlaps", False) and len(heatmaps_list) > 1:
            heatmap_final = self.overlaps(
                heatmaps_list, min_overlaps=len(heatmaps_list)
            )
        else:
            heatmap_final = np.sum(heatmaps_list, axis=0)

        heatmap_final = gaussian_filter(
            heatmap_final, sigma=params["gaussian_sigma"] // 2
        )
        heatmap_final = self.colormap_manager.apply_enhancement(
            heatmap_final,
            gamma=params["gamma"],
            alpha=params["alpha"],
            contrast=params["contrast"],
        )

        self.original_heatmap_data = heatmap_final.copy()
        if self.colormap_manager.should_invert_for_opencv(params["colormap_name"]):
            heatmap_final = 1.0 - heatmap_final

        self.heatmap_data = heatmap_final.copy()

        heatmap_uint8 = np.uint8(255 * heatmap_final)
        heatmap_color = self.colormap_manager.apply_colormap_cv2_simple(
            heatmap_uint8, params["colormap_name"]
        )

        if params["markup"]:
            self.time_matrix = time_matrix
            heatmap_color = self.draw_grid_with_time(
                heatmap_color=heatmap_color,
                time_matrix=time_matrix,
                grid_color=(255, 255, 255),
                text_color=(255, 255, 255),
                alpha=0.9,
            )
        self.mode = data.iloc[0]["mode"]
        self.data = data
        if params["platform_allowed"]:
            heatmap_color = self._draw_platform(
                data,
                heatmap_color,
                params["rgb_values"],
                center_shift_cm,
                resolution,
                SIZE_PX,
            )

        if params["is_add_colorbar"]:
            heatmap_color = self.colormap_manager.add_colorbar(
                heatmap_color, params["colormap_name"]
            )  # , vmin=heatmap.min(), vmax=heatmap.max()

        image = self.create_qimage(heatmap_color)
        self.widget_ui.set_image(image)

    def update_time_matrix(
        self, time_matrix, bbox, fps, block_height, block_width, grid_size, size_px
    ):
        x1, y1, x2, y2 = bbox
        bbox_area = (x2 - x1) * (y2 - y1)

        for i in range(grid_size):
            for j in range(grid_size):
                y_start = i * block_height
                y_end = (i + 1) * block_height if i < grid_size - 1 else size_px
                x_start = j * block_width
                x_end = (j + 1) * block_width if j < grid_size - 1 else size_px

                # Просчитать пересечение
                x_overlap = max(0, min(x2, x_end) - max(x1, x_start))
                y_overlap = max(0, min(y2, y_end) - max(y1, y_start))
                overlap_area = x_overlap * y_overlap

                if overlap_area > 0 and bbox_area > 0:
                    time_matrix[i, j] += overlap_area / (fps * bbox_area)

    def overlaps(self, matrices, min_overlaps=None):
        if not matrices:
            return np.zeros_like(matrices[0]) if matrices else None

        if min_overlaps is None:
            min_overlaps = len(matrices)

        binary_masks = []
        for mat in matrices:
            if np.max(mat) > 0:
                normalized = mat / np.max(mat)
                threshold = 0.001
                binary_mask = normalized > threshold
            else:
                binary_mask = np.zeros_like(mat, dtype=bool)
            binary_masks.append(binary_mask)

        stacked_masks = np.stack(binary_masks)
        overlap_mask = np.all(stacked_masks, axis=0)

        stacked_values = np.stack(matrices)
        result = np.where(overlap_mask, np.sum(stacked_values, axis=0), 0)

        return result

    def _draw_platform(
        self, data, heatmap_color, rgb_values, center_shift_cm, resolution, SIZE_PX
    ):
        pixel_size = data.iloc[0]["pixel_size"]
        center_x_data = data.iloc[0]["center_x"]
        center_y_data = data.iloc[0]["center_y"]

        dx_cm = center_shift_cm - center_x_data * pixel_size
        dy_cm = center_shift_cm - center_y_data * pixel_size

        points = data.iloc[0]["p"]
        # print(f"DEBUG: points = {points}")
        for point in points:
            second_point_x_cm = point[0] * pixel_size
            second_point_y_cm = point[1] * pixel_size

            center_x = int((second_point_x_cm + dx_cm) * resolution)
            center_y = int((second_point_y_cm + dy_cm) * resolution)
            platform_radius_cm = data.iloc[0]["areaInt"]
            radius = int(platform_radius_cm * resolution) // 2

            center_x = max(radius, min(SIZE_PX - radius, center_x))
            center_y = max(radius, min(SIZE_PX - radius, center_y))

            cv2.circle(
                heatmap_color,
                (center_x, center_y),
                radius,
                rgb_values[::-1],
                thickness=-1,
            )
        return heatmap_color

    def draw_grid_with_time(
        self,
        heatmap_color,
        time_matrix=None,
        grid_color=(255, 255, 255),
        text_color=(255, 255, 255),
        alpha=0.7,
    ):
        overlay = heatmap_color.copy()
        h, w = overlay.shape[:2]
        grid_size = 3

        thickness = max(3, int(min(h, w) * 0.005))

        for i in range(1, grid_size):
            x = int(w * i / grid_size)
            cv2.line(overlay, (x, 0), (x, h), grid_color, thickness)
            y = int(h * i / grid_size)
            cv2.line(overlay, (0, y), (w, y), grid_color, thickness)

        if time_matrix is not None:
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = min(h, w) * 0.002

            for i in range(grid_size):
                for j in range(grid_size):
                    x_center = int(w * (j + 0.5) / grid_size)
                    y_center = int(h * (i + 0.5) / grid_size)
                    time_text = f"{time_matrix[i, j]:.1f}s"

                    text_size = cv2.getTextSize(time_text, font, font_scale, 2)[0]
                    text_x = x_center - text_size[0] // 2
                    text_y = y_center + text_size[1] // 2

                    cv2.putText(
                        overlay,
                        time_text,
                        (text_x, text_y),
                        font,
                        font_scale,
                        (0, 0, 0),
                        thickness + 3,
                        cv2.LINE_AA,
                    )
                    cv2.putText(
                        overlay,
                        time_text,
                        (text_x, text_y),
                        font,
                        font_scale,
                        text_color,
                        thickness,
                        cv2.LINE_AA,
                    )

        return cv2.addWeighted(overlay, alpha, heatmap_color, 1 - alpha, 0)

    def create_qimage(self, cv_image):
        height, width, _ = cv_image.shape
        bytes_per_line = 3 * width
        return QImage(
            cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()

    @Slot(QImage)
    def on_save_image(self, image):
        dialog = SaveImgaeDialog(image, self.save_path, "heatmap")
        dialog.exec()

    def get_configuration(self):
        new_settings = self.widget_ui.collect_settings()
        self.heatmap_configure = self.heatmap_configure.model_copy(update=new_settings)
        return self.heatmap_configure

import cv2
import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.interpolate import interp1d


class ColormapManager:
    def __init__(self):
        self._setup_unified_colormaps()

    def _setup_unified_colormaps(self):
        self.unified_colormaps = {}

        self.inverted_direction_colormaps = {
            "viridis",
            "plasma",
            "inferno",
            "magma",
            "cividis",
        }

        base_colormaps = {
            "jet": cv2.COLORMAP_JET,
            "viridis": cv2.COLORMAP_VIRIDIS,
            "plasma": cv2.COLORMAP_PLASMA,
            "inferno": cv2.COLORMAP_INFERNO,
            "magma": cv2.COLORMAP_MAGMA,
            "cividis": cv2.COLORMAP_CIVIDIS,
            "hot": cv2.COLORMAP_HOT,
            "cool": cv2.COLORMAP_COOL,
            "spring": cv2.COLORMAP_SPRING,
            "autumn": cv2.COLORMAP_AUTUMN,
            "winter": cv2.COLORMAP_WINTER,
            "bone": cv2.COLORMAP_BONE,
            "rainbow": cv2.COLORMAP_RAINBOW,
            "ocean": cv2.COLORMAP_OCEAN,
            "summer": cv2.COLORMAP_SUMMER,
            "pink": cv2.COLORMAP_PINK,
            "turbo": cv2.COLORMAP_TURBO,
        }

        for name, cv2_cmap in base_colormaps.items():
            lut = self._create_cv2_lut_from_cv2(
                cv2_cmap, invert=(name in self.inverted_direction_colormaps)
            )
            self.unified_colormaps[name] = {"cv2_lut": lut}

        self.unified_colormaps["custom_jet"] = {
            "cv2_lut": self._create_custom_jet_lut()
        }

    def _create_cv2_lut_from_cv2(self, cv2_colormap, invert=False):
        gradient = np.arange(256, dtype=np.uint8)

        if invert:
            gradient = 255 - gradient

        gradient = gradient.reshape((256, 1))
        return cv2.applyColorMap(gradient, cv2_colormap)

    def _create_custom_jet_lut(self):
        red_points = [(0.00, 0), (0.35, 0), (0.66, 1), (0.89, 1), (1.00, 0.5)]
        green_points = [
            (0.00, 0),
            (0.125, 0),
            (0.375, 1),
            (0.64, 1),
            (0.91, 0),
            (1.00, 0),
        ]
        blue_points = [
            (0.00, 0),
            (0.05, 0.25),
            (0.15, 1),
            (0.34, 1),
            (0.65, 0),
            (1.00, 0),
        ]

        def prepare_interpolator(points):
            x_vals, y_vals = zip(*points)
            return interp1d(
                x_vals,
                y_vals,
                kind="cubic",
                bounds_error=False,
                fill_value=(y_vals[0], y_vals[-1]),
            )

        interp_r = prepare_interpolator(red_points)
        interp_g = prepare_interpolator(green_points)
        interp_b = prepare_interpolator(blue_points)

        # Создаем LUT
        lut = np.zeros((256, 1, 3), dtype=np.uint8)
        x = np.linspace(0, 1, 256)

        r = np.clip(interp_r(x), 0, 1)
        g = np.clip(interp_g(x), 0, 1)
        b = np.clip(interp_b(x), 0, 1)

        lut[:, 0, 0] = (b * 255).astype(np.uint8)
        lut[:, 0, 1] = (g * 255).astype(np.uint8)
        lut[:, 0, 2] = (r * 255).astype(np.uint8)

        return lut

    def get_available_colormaps(self):
        return list(self.unified_colormaps.keys())

    def get_colormap(self, key):
        return self.base

    def should_invert_for_opencv(self, colormap_name):
        return colormap_name in self.inverted_direction_colormaps

    def apply_colormap_cv2_simple(self, heatmap_uint8, colormap_name):
        if colormap_name not in self.unified_colormaps:
            colormap_name = "jet"

        lut = self.unified_colormaps[colormap_name]["cv2_lut"]

        if heatmap_uint8.ndim == 2:
            return cv2.applyColorMap(heatmap_uint8, lut)

        if heatmap_uint8.ndim == 3 and heatmap_uint8.shape[2] == 1:
            return cv2.applyColorMap(heatmap_uint8.squeeze(), lut)

        if heatmap_uint8.ndim == 3 and heatmap_uint8.shape[2] == 3:
            return heatmap_uint8

        return cv2.LUT(heatmap_uint8, lut)

    def apply_enhancement(
        self, heatmap_data, gamma=1.0, alpha=1.0, contrast=1.0, clarity=1.0
    ):
        heatmap_data = np.asarray(heatmap_data, dtype=np.float32)

        min_val = heatmap_data.min()
        max_val = heatmap_data.max()

        norm = (heatmap_data - min_val) / (max_val - min_val + 1e-8)

        if contrast != 1.0:
            norm = np.clip((norm - 0.5) * contrast + 0.5, 0, 1)

        if gamma != 1.0:
            norm = np.power(norm, gamma)

        if alpha != 1.0:
            norm = np.clip(norm * alpha, 0, 1)

        if clarity > 1.0:
            blurred = gaussian_filter(norm, sigma=1.0)
            norm = np.clip(norm + (norm - blurred) * (clarity - 1.0), 0, 1)

        return norm

    def add_colorbar(self, image_bgr, colormap_name, ticks=6, vertical_padding=0.02):

        if colormap_name not in self.unified_colormaps:
            colormap_name = "jet"

        lut = self.unified_colormaps[colormap_name]["cv2_lut"]

        h, w = image_bgr.shape[:2]

        padding_px = int(h * max(0.0, min(0.4, vertical_padding)))
        bar_h = h - 2 * padding_px

        scale = np.sqrt(h / 512.0)
        scale = np.clip(scale, 1.0, 3.5)

        bar_width = int(40 * scale)
        padding = int(20 * scale)
        font_scale = 0.85 * scale
        thickness = max(1, int(1 + scale))
        tick_len = int(bar_width * 0.25)

        gradient = np.linspace(255, 0, bar_h, dtype=np.uint8).reshape(bar_h, 1)
        if colormap_name in self.inverted_direction_colormaps:
            gradient = np.linspace(0, 255, bar_h, dtype=np.uint8).reshape(bar_h, 1)

        colorbar = cv2.applyColorMap(gradient, lut)
        colorbar = cv2.resize(
            colorbar, (bar_width, bar_h), interpolation=cv2.INTER_NEAREST
        )

        canvas_w = w + padding + bar_width + int(bar_width * 2.0)
        canvas = np.full((h, canvas_w, 3), 255, dtype=np.uint8)

        canvas[:, :w] = image_bgr
        bar_x = w + padding

        canvas[padding_px : padding_px + bar_h, bar_x : bar_x + bar_width] = colorbar

        cv2.rectangle(
            canvas,
            (bar_x, padding_px),
            (bar_x + bar_width - 1, padding_px + bar_h - 1),
            (0, 0, 0),
            thickness,
        )

        for i in range(ticks):
            t = i / (ticks - 1)
            y = padding_px + int((1.0 - t) * (bar_h - 1))
            value = t
            cv2.line(
                canvas,
                (bar_x + bar_width, y),
                (bar_x + bar_width + tick_len, y),
                (0, 0, 0),
                thickness,
            )

            cv2.putText(
                canvas,
                f"{value:.2f}",
                (bar_x + bar_width + tick_len + 10, y + int(font_scale * 12)),
                cv2.FONT_HERSHEY_SIMPLEX,
                font_scale,
                (0, 0, 0),
                thickness,
                cv2.LINE_AA,
            )

        return canvas

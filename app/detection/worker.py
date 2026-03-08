from PySide6.QtCore import QObject, Signal
from pathlib import Path
import pandas as pd
import cv2
import torch
import numpy as np

class DetectionWorker(QObject):
    progress = Signal(int)
    finished = Signal(dict)
    error = Signal(str)

    def __init__(self, video_path, out, model, model_type: str):
        super().__init__()
        self.video_path = video_path
        self.out = out
        self.model = model
        self.model_type = model_type
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def _setup_signals(self,):
        self.worker.progress.connect(self.progress)
        self.worker.finished.connect(self.on_finished)
        self.worker.error.connect(self.error)

    def run(self):
        try:
            print("Обработка начата")
            result_det = self.process_video(
                path=self.video_path
            )
            print("Обработка завершена")
            csv_name = Path(self.video_path).stem + "_data.csv"

            self.finished.emit({
                "csv_name": csv_name,
                "data": pd.DataFrame(result_det)
            })
            
        except Exception as e:
            self.error.emit(str(e))


    def process_video(self, path: str):
        cap = cv2.VideoCapture(path)
        results = []

        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        idx = 0
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                res = self.infer_frame(frame)
                results.append(res)

                if self.out is not None:
                    frame_annotated = frame.copy()
                    box_coords = res.get("box", None)
                    if box_coords:
                        cv2.rectangle(frame_annotated,
                                    (box_coords[0], box_coords[1]),
                                    (box_coords[2], box_coords[3]),
                                    (0, 0, 255), 1)
                    self.out.write(frame_annotated)

                idx += 1
                progress_percent = int((idx / total) * 100)
                self.progress.emit(progress_percent)

            cap.release()
            if self.out is not None:
                self.out.release()

        except Exception as e:
            print(e)
        finally:
            return results

    def infer_frame(self, frame: np.ndarray) -> dict:
        h, w = frame.shape[:2]

        if self.model_type == "yolo":
            resized = cv2.resize(frame, (256, 256))
            result = self.model(resized, verbose=False)[0]

            if len(result.boxes) == 0:
                return self._empty_result()

            x1, y1, x2, y2 = result.boxes.xyxy[0].cpu().numpy()

            # масштаб обратно
            x1 *= w / 256
            x2 *= w / 256
            y1 *= h / 256
            y2 *= h / 256

            return self._build_result(x1, y1, x2, y2)

        if self.model_type == "FRCNN":
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            tensor = torch.from_numpy(img).permute(2, 0, 1).float() / 255
            tensor = tensor.unsqueeze(0).to(self.device)

            with torch.no_grad():
                pred = self.model(tensor)[0]

            keep = (pred["scores"] > 0.7) & (pred["labels"] == 1)
            if keep.sum() == 0:
                return self._empty_result()

            x1, y1, x2, y2 = pred["boxes"][keep][0].cpu().numpy()
            return self._build_result(x1, y1, x2, y2)

        raise ValueError("Unknown model type")

    def _build_result(self, x1, y1, x2, y2):
        return {
            "xc": (x1 + x2) / 2,
            "yc": (y1 + y2) / 2,
            "width": x2 - x1,
            "height": y2 - y1,
            "box": (int(x1), int(y1), int(x2), int(y2))
        }

    def _empty_result(self):
        return {
            "xc": 0,
            "yc": 0,
            "width": 0,
            "height": 0,
            "box": None
        }


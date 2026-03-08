from typing import Tuple

from .loaders import ModelLoaders
from .embedded_models import (
    best_fasterrcnn_bytes,
    best_op_pkl_bytes,
    best_morris_black_bytes,
    best_morris_white_bytes,
    best_ldt_bytes,
    best_ymt_bytes,
    best_tcs_bytes,
)

class DetectionModelFactory:

    _YOLO_MAP = {
        "op_pkl": best_op_pkl_bytes,
        "morris_black": best_morris_black_bytes,
        "morris_white": best_morris_white_bytes,
        "ldt": best_ldt_bytes,
        "ymt": best_ymt_bytes,
        "tcs": best_tcs_bytes,
    }

    @classmethod
    def create(cls, mode: str) -> Tuple[object, str]:
        if mode == "auto":
            model = ModelLoaders.load_fasterrcnn_from_embedded(
                best_fasterrcnn_bytes
            )
            return model, "FRCNN"

        if mode in cls._YOLO_MAP:
            yolo_data = cls._YOLO_MAP[mode]
            # print(f"DEBUG: YOLO data for mode '{mode}' type = {type(yolo_data)}")
            # print(f"DEBUG: YOLO data = {yolo_data[:50] if isinstance(yolo_data, (str, bytes)) else yolo_data}")

            model = ModelLoaders.load_yolo_from_embedded(yolo_data)
            return model, "yolo"

        raise ValueError(f"Unknown detection mode: {mode}")

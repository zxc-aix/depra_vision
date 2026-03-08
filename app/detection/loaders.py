from typing import Tuple
import base64, zlib, io, tempfile, torch
from ultralytics import YOLO
from typing import Optional, Union
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

class ModelLoaders:

    @staticmethod
    def load_yolo_from_embedded(encoded: str) -> YOLO:

        raw = zlib.decompress(base64.b64decode(encoded))
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pt") as tmp:
            tmp.write(raw)
            tmp.flush()
            path = tmp.name

        model = YOLO(path)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)
        return model

    @staticmethod
    def load_fasterrcnn_from_embedded(encoded: str) -> torch.nn.Module:

        raw = zlib.decompress(base64.b64decode(encoded))
        buffer = io.BytesIO(raw)
        state_dict = torch.load(buffer, map_location="cpu", weights_only=True)

        model = fasterrcnn_resnet50_fpn(weights=None)
        in_features = model.roi_heads.box_predictor.cls_score.in_features
        model.roi_heads.box_predictor = FastRCNNPredictor(in_features, 2)

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.load_state_dict(state_dict)
        model.to(device)
        model.eval()

        return model
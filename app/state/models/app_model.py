from pydantic import BaseModel
from typing import Optional, Dict, Any

class AppModel(BaseModel):
    videos_dir: Optional[str] = "videos"
    predictions_dir: Optional[str] = "predictions"
    trajectory_dir: Optional[str] = "predictions"
    heatmap_dir: Optional[str] = "predictions"
    language: Optional[str] = "ru"
    theme: Optional[str] = "Fusion"
    set_annotated_video: Optional[bool] = False

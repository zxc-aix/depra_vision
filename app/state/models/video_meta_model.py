from pydantic import BaseModel
from typing import Optional

class VideoMetaModel(BaseModel):
    video_name: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    fps: Optional[float] = None
    fourcc: Optional[float] = None
    frame_count: Optional[int] = None
    valid: bool = False
    date: Optional[str] = None
    time: Optional[str] = None
    current_path: Optional[str] = None
    is_annotated: Optional[bool] = False
    annotate_dir: Optional[str] = None
from pydantic import BaseModel
from typing import Optional, Dict, Any

class HeatmapModel(BaseModel):
    zoom: Optional[float] = 1.0
    box_scale: Optional[float] = 1.0
    gamma: Optional[float] = 1.0
    alpha: Optional[float] = 1.0
    gaussian_sigma: Optional[int] = 70
    contrast: Optional[float] = 1.0
    is_add_colorbar: Optional[bool] = False
    platform_allowed: Optional[bool] = False
    markup: Optional[bool] = False
    overlaps: Optional[bool] = False
    interpolate: Optional[bool] = False
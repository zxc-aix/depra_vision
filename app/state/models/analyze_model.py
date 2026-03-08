from pydantic import BaseModel
from typing import Optional, Dict, Any

class AnalysisModel(BaseModel):
    ShStEn: Optional[bool] = False
    DiveTraj: Optional[bool] = False
    AddZones: Optional[bool] = False
    Scale: Optional[float] = 1.0
    ThError: Optional[float] = 1.0
    speed_threshold: Optional[float] = 7.5
    freeze_threshold: Optional[float] = 1.5
    min_freeze_duration: Optional[float] = 2.0
    Wrap: Optional[bool] = False
    BuildBr: Optional[bool] = False
    Thick: Optional[float] = 1.0
    AngleDist: Optional[float] = 1.0
    AngleTime: Optional[float] = 1.0
    AnglePer: Optional[float] = 1.0
    TimeStart: Optional[float] = 0.0
    TimeEnd: Optional[float] = 0.0
    T0: Optional[float] = 0.0
    T1: Optional[float] = 1.0
    T2: Optional[float] = 2.0
    T3: Optional[float] = 3.0
    WidthTraj: Optional[float] = 1.0
    WidthMarkup: Optional[float] = 1.0
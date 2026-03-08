from pydantic import BaseModel
from typing import Optional, Dict, Any

class FieldModel(BaseModel):
    pixel_size: Optional[float] = None
    distance_pixel: Optional[float] = None
    mode: Optional[str] = None
    model: Optional[str] = "auto"
    field_size: Optional[Any] = None

    p_center: Optional[tuple[float, float]] = None
    p: Optional[list[tuple[float, float]]] = None

    scale: Optional[float] = None

    box: Optional[Dict] = {
        "small" : 10, 
        "medium" : 25, 
        "large" : 40,
        "countObject": 0,
        "areaInt": 0,
    }
    cross: Optional[Dict] = {
        "widthArms": 6,
        "lengthArms": 16,
        "center" : False, 
        "up" : False, 
        "right" : False,
        "down" : False, 
        "left" : False, 
        "outside" : False
    }
    morris: Optional[Dict] = {
        "areaInt": 10,
        "space": 150,
        "custom_fields": [],
        "angle": 0,
        "diam": 0
    }
    ymt: Optional[Dict] = {
        "widthArms": 8,
        "lengthArms": 32.5,
        "angleArms": 0,
        "countObject": 0,
        "areaInt": 0,
        "alpha1": 0,
        "alpha2": 120,
        "alpha3": 240
    }
    ldt: Optional[Dict] = {
        "widthArmsLight": 20,
        "lengthArmsLight": 40,
        "widthArmsDark": 20,
        "lengthArmsDark": 40,
        "radius": 0,
        "SizePass": 5,
        "has_dark_room": False
    }
    tcs: Optional[Dict] = {
        "width": 40,
        "length": 40,
        "length_left": 10,
        "length_right": 10,
        "countObject": 0,
        "areaInt": 0,
        "SizePass": 0
    }
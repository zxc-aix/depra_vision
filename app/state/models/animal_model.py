from pydantic import BaseModel
from typing import Optional, Dict, Any

class AnimalModel(BaseModel):
    id: Optional[str] = None
    age: Optional[str] = None
    weight: Optional[str] = None
    color: Optional[str] = None
    type: Optional[str] = None
    model: Optional[str] = None
    line: Optional[str] = None
    subline: Optional[str] = None
    count_animal: int = 1
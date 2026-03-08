from pydantic import BaseModel

from .analyze_model import AnalysisModel
from .animal_model import AnimalModel
from .app_model import AppModel
from .field_model import FieldModel
from .heatmap_model import HeatmapModel
from .video_meta_model import VideoMetaModel

class AppState(BaseModel):
    app: AppModel = AppModel()
    video: VideoMetaModel = VideoMetaModel()
    field: FieldModel = FieldModel()
    analysis: AnalysisModel = AnalysisModel()
    heatmap: HeatmapModel = HeatmapModel()
    animal: AnimalModel = AnimalModel()
from PySide6.QtCore import QObject, Signal
from app.state.models import AppState, VideoMetaModel, FieldModel, AnalysisModel, HeatmapModel, AnimalModel, AppModel

class StateManager(QObject):
    state_changed = Signal(AppState)
    video_changed = Signal(VideoMetaModel)
    animal_changed = Signal(AnimalModel)
    field_changed = Signal(FieldModel)
    heatmap_changed = Signal(HeatmapModel)
    analysis_changed = Signal(AnalysisModel)
    app_changed = Signal(AppModel)

    def __init__(self):
        super().__init__()
        self._state = AppState()

    @property
    def state(self) -> AppState:
        return self._state

    @property
    def app(self) -> AppModel:
        return self._state.app
    
    @property
    def video(self) -> VideoMetaModel:
        return self._state.video

    @property
    def field(self) -> FieldModel:
        return self._state.field

    @property
    def animal(self) -> AnimalModel:
        return self._state.animal

    @property
    def heatmap(self) -> HeatmapModel:
        return self._state.heatmap

    @property
    def analysis(self) -> AnalysisModel:
        return self._state.analysis
    
    def update_app(self, **kwargs):
        new = self._state.app.copy(update=kwargs)
        self._state = self._state.copy(update={"app": new})

        self.app_changed.emit(self._state)
        self.state_changed.emit(self._state)

    def update_video(self, **kwargs):
        new = self._state.video.copy(update=kwargs)
        self._state = self._state.copy(update={"video": new})

        self.video_changed.emit(new)
        self.state_changed.emit(self._state)

    def update_field(self, **kwargs):
        new = self._state.field.copy(update=kwargs)
        self._state = self._state.copy(update={"field": new})

        self.field_changed.emit(new)
        self.state_changed.emit(self._state)

    def update_animal(self, **kwargs):
        new = self._state.animal.copy(update=kwargs)
        self._state = self._state.copy(update={"animal": new})

        self.animal_changed.emit(new)
        self.state_changed.emit(self._state)

    def update_heatmap(self, **kwargs):
        new = self._state.heatmap.copy(update=kwargs)
        self._state = self._state.copy(update={"heatmap": new})

        self.heatmap_changed.emit(new)
        self.state_changed.emit(self._state)

    def update_analysis(self, **kwargs):
        new = self._state.analysis.copy(update=kwargs)
        self._state = self._state.copy(update={"analysis": new})

        self.analysis_changed.emit(new)
        self.state_changed.emit(self._state)
    

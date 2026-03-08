from pathlib import Path

from PySide6.QtWidgets import QMessageBox

from app.analysis.report import Builder
from app.ui.dialogs import OutputResultsDialog


class OutputResultsController:
    def __init__(self, mode, video_configure, animal_configure, field_configure, stats, save_dir="./predictions/", language="en"):
        self.mode = mode
        self.video_cfg = video_configure
        self.animal_cfg = animal_configure
        self.field_cfg = field_configure
        self.stats = stats
        self.language = language
        self.save_dir = save_dir

    def run(self):
        try:
            builder = Builder(
                mode=self.mode, video=self.video_cfg, animal=self.animal_cfg, field=self.field_cfg,
                results=self.stats, language=self.language
            )
            rows = builder.build()

            save_path = self._make_save_path(self.save_dir)

            dialog = OutputResultsDialog(rows, save_path)
            if dialog.exec():
                print("DEBUG: Отчёт сохранён")
            else:
                print("DEBUG: Пользователь отменил")

        except Exception as e:
            QMessageBox.critical(
                None,
                "Ошибка формирования отчёта",
                str(e)
            )

    def _make_save_path(self, save_dir):
        base = Path(save_dir) / "stats_files"
        base.mkdir(exist_ok=True)
        return base / "report.xlsx"

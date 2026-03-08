from .schema import BOX_SCHEMA, CROSS_SCHEMA, MORRIS_SCHEMA, YMT_SCHEMA, TCS_SCHEMA, LDT_SCHEMA 
import pandas as pd
from pathlib import Path

class ReportBuilder:
    def __init__(self, mode, video: dict, animal: dict, field: dict, results: dict, language: str = "ru"):
        self.schema = self.get_schema(mode)
        self.sources = {
            "video": video or {},
            "animal": animal or {},
            "field": field or {},
            "results": results or {},
            "manual": {}
        }
        self.language = language

    def build(self) -> list[dict]:
        rows = []
        print(f"DEBUG: lang = {self.language}")
        for field in self.schema:
            src = self.sources[field.source]
            # print(f"DEBUG: src = {src}")
            value = (
                src.get(field.value_key, field.default)
                if field.value_key
                else field.default
            )

            if field.formatter and value is not None:
                value = field.formatter(value)

            rows.append({
                "key": field.key,
                "label": field.label[self.language],
                "value": value,
                "editable": field.source == "manual"
            })

        return rows
    
    def get_schema(self, mode):
        if mode == "box":
            return BOX_SCHEMA
        elif mode == "cross":
            return CROSS_SCHEMA
        elif mode == "morris":
            return MORRIS_SCHEMA
        elif mode == "ymt":
            return YMT_SCHEMA
        elif mode == "ldt":
            return LDT_SCHEMA
        elif mode == "tcs":
            return TCS_SCHEMA
        else:
            raise ValueError(f"Unknown analysis mode: {mode}")
        
class ReportExporter:
    @staticmethod
    def to_dataframe(rows: list[dict]) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "Parameter": [r["label"] for r in rows],
                "Type": ["manual" if r["editable"] else "auto" for r in rows],
                "Value": [r["value"] for r in rows],
            }
        )

    @staticmethod
    def to_csv(df: pd.DataFrame, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)

    @staticmethod
    def to_excel(df: pd.DataFrame, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_excel(path, index=False)


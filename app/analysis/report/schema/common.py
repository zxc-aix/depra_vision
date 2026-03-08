from dataclasses import dataclass
from typing import Callable, Any

@dataclass(frozen=True)
class ReportField:
    key: str
    label: dict # {"ru": "...", "en": "..."}
    source: str # video | animal | field | results | manual
    value_key: str | None = None
    formatter: Callable[[Any], Any] | None = None
    default: dict[str, Any] | Any = None 


COMMON_SCHEMA = [
    # file info
    ReportField(
        key="test_id",
        label={"ru": "ID исследования", "en": "ID research"},
        source="manual",
        default=""
    ),
    ReportField(
        key="video_name",
        label={"ru": "Название файла", "en": "File name"},
        source="video",
        value_key="video_name"
    ),
    ReportField(
        key="test_type",
        label={"ru": "Тип теста", "en": "Test type"},
        source="field",
        value_key="mode"
    ),
    ReportField(
        key="test_specification",
        label={"ru": "Спецификация теста", "en": "Test specification"},
        source="manual",
        default=""
    ),
    ReportField(
        key="test_date",
        label={"ru": "Дата проведения теста", "en": "Test date"},
        source="video",
        value_key="date"
    ),
    ReportField(
        key="test_id",
        label={"ru": "Освещения, люкс", "en": "Lighting, suite"},
        source="manual",
        default=""
    ),
    ReportField(
        key="total_time",
        label={"ru": "Общее время теста, с", "en": "Total test time, c"},
        source="results",
        value_key="total_time",
        formatter=lambda v: f"{v:.1f}",
    ),
    ReportField(
        key="test_time",
        label={"ru": "Время проведения теста", "en": "Test time"},
        source="video",
        value_key="time"
    ),
    ReportField(
        key="test_name",
        label={"ru": "Название эксперимента", "en": "Name of experiment"},
        source="manual",
        default=""
    ),
    ReportField(
        key="animal_count",
        label={"ru": "Число животных в тесте", "en": "Number of animals in test"},
        source="animal",
        value_key="count_animal"
    ),
    ReportField(
        key="researcher_name",
        label={"ru": "Имя исследователя", "en": "Researcher"},
        source="manual",
        default=""
    ),

    # anmal
    ReportField(
        key="animal_id",
        label={"ru": "Индивидуальный номер животного", "en": "Animal ID"},
        source="animal",
        value_key="id",
        default="Not stated"
    ),
    ReportField(
        key="animal_age",
        label={"ru": "Возраст животного, нед.", "en": "Age of animal, weeks"},
        source="animal",
        value_key="age",
        default="Not stated"
    ),
    ReportField(
        key="animal_weight",
        label={"ru": "Вес животного, г", "en": "Weight, g"},
        source="animal",
        value_key="weight",
        default="Not stated"
    ),
    ReportField(
        key="animal_gender",
        label={"ru": "Пол животного", "en": "Gender of the animal"},
        source="manual",
        default=""
    ),
    ReportField(
        key="animal_type",
        label={"ru": "Вид животного", "en": "Type of animal"},
        source="animal",
        value_key="type",
        default="Not stated"
    ),
    ReportField(
        key="animal_model",
        label={"ru": "Модель животного", "en": "Model of animal"},
        source="animal",
        value_key="model",
        default="Not stated"
    ),
    ReportField(
        key="animal_line",
        label={"ru": "Линия животного", "en": "Line of animal"},
        source="animal",
        value_key="line",
        default="Not stated"
    ),
    ReportField(
        key="animal_subline",
        label={"ru": "Подлиния животного", "en": "Subline of animal"},
        source="manual",
        value_key="subline",
        default="Not stated"
    ),
]

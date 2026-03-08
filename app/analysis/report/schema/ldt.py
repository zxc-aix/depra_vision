from .common import ReportField, COMMON_SCHEMA

LDT_SCHEMA = COMMON_SCHEMA + [
    # distance
    ReportField(
        key="total_distance",
        label={"ru": "Общая дистанция, см", "en": "Total distance, cm"},
        source="results",
        value_key="total_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_outside",
        label={"ru": "Дистанция вне полей, см", "en": "Distance outside fields, cm"},
        source="results",
        value_key="distance_outside",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_light",
        label={"ru": "Дистанция в светлом поле, см", "en": "Distance in light field, cm"},
        source="results",
        value_key="distance_light",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_dark",
        label={"ru": "Дистанция в темном поле, см", "en": "Distance in dark field, cm"},
        source="results",
        value_key="distance_dark",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    # time
    ReportField(
        key="time_outside",
        label={"ru": "Время вне полей, см", "en": "Time outside fields, cm"},
        source="results",
        value_key="time_outside",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_light",
        label={"ru": "Время в светлом поле, с", "en": "Time in light field, s"},
        source="results",
        value_key="time_light",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_dark",
        label={"ru": "Время в темном поле, с", "en": "Time in dark field, s"},
        source="results",
        value_key="time_dark",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    # transit
    ReportField(
        key="total_transitions",
        label={"ru": "Число переходов между всеми полями, у.е.", "en": "Number of transitions between all fields, units"},
        source="results",
        value_key="total_transitions",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_light_dark",
        label={"ru": "Число переходов между светлым и темныс полями, у.е.", "en": "Number of transitions between light and dark fields, units"},
        source="results",
        value_key="transitions_light_dark",
        formatter=lambda v: f"{v}",
        default=0
    ),

    # ratio
    ReportField(
        key="time_light_ratio",
        label={"ru": "Доля времени в светлом поле от общего, %", "en": "Proportion of time in light field to total, %"},
        source="results",
        value_key="time_light_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_dark_ratio",
        label={"ru": "Доля времени в темном поле от общего, %", "en": "Proportion of time in dark field to total, %"},
        source="results",
        value_key="time_dark_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_light_ratio",
        label={"ru": "Доля дистанции в светлом поле от общей, %", "en": "Proportion of distance in light field to total, %"},
        source="results",
        value_key="distance_light_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_dark_ratio",
        label={"ru": "Доля дистанции в темном поле от общей, %", "en": "Proportion of distance in dark field to total, %"},
        source="results",
        value_key="distance_dark_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    # if there is
    ReportField(
        key="visits_in_1",
        label={"ru": "Пересечение зоны 1", "en": "Zone 1 crossings"},
        source="results",
        value_key="visits_in_1",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="distance_in_1",
        label={"ru": "Дистанция в зоне 1, см", "en": "Distance in zone 1, cm"},
        source="results",
        value_key="distance_in_1",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_1",
        label={"ru": "Время в зоне 1, с", "en": "Time in zone 1, s"},
        source="results",
        value_key="time_in_1",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_1",
        label={"ru": "Скорость в зоне 1, см/с", "en": "Speed in zone 1, cm/s"},
        source="results",
        value_key="speed_in_1",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
]
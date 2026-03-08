from .common import ReportField, COMMON_SCHEMA

TCS_SCHEMA = COMMON_SCHEMA + [
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
        key="distance_left",
        label={"ru": "Дистанция в левом поле, см", "en": "Distance in left field, cm"},
        source="results",
        value_key="distance_left",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_right",
        label={"ru": "Дистанция в правом поле, см", "en": "Distance in right field, cm"},
        source="results",
        value_key="distance_right",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_center",
        label={"ru": "Дистанция в средем поле, см", "en": "Distance in middle field, cm"},
        source="results",
        value_key="distance_center",
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
        key="time_left",
        label={"ru": "Время в левом поле, с", "en": "Time in left field, s"},
        source="results",
        value_key="time_left",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_right",
        label={"ru": "Время в правом поле, с", "en": "Time in right field, s"},
        source="results",
        value_key="time_right",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_center",
        label={"ru": "Время в среднем поле, с", "en": "Time in middle field, s"},
        source="results",
        value_key="time_center",
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
        key="transitions_left_right",
        label={"ru": "Число переходов между левым и правым полями, у.е.", "en": "Number of transitions between left and right fields, units"},
        source="results",
        value_key="transitions_left_right",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_left_center",
        label={"ru": "исло переходов между левым и центральным полями, у.е.", "en": "Number of transitions between left and central fields, units"},
        source="results",
        value_key="transitions_left_center",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_center_right",
        label={"ru": "исло переходов между центральным и правым полями, у.е.", "en": "Number of transitions between central and right fields, units"},
        source="results",
        value_key="transitions_center_right",
        formatter=lambda v: f"{v}",
        default=0
    ),

    # ratio
    ReportField(
        key="time_left_ratio",
        label={"ru": "Доля времени в левом поле от общего, %", "en": "Proportion of time in left field to total, %"},
        source="results",
        value_key="time_left_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_right_ratio",
        label={"ru": "Доля времени в правом поле от общего, %", "en": "Proportion of time in right field to total, %"},
        source="results",
        value_key="time_right_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_center_ratio",
        label={"ru": "Доля времени в средем поле от общего, %", "en": "Proportion of time in middle field to total, %"},
        source="results",
        value_key="time_center_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_left_ratio",
        label={"ru": "Доля дистанции в левом поле от общей, %", "en": "Proportion of distance in left field to total, %"},
        source="results",
        value_key="distance_left_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_right_ratio",
        label={"ru": "Доля дистанции в правом поле от общей, %", "en": "Proportion of distance in right field to total, %"},
        source="results",
        value_key="distance_right_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_center_ratio",
        label={"ru": "Доля дистанции в средем поле от общей, %", "en": "Proportion of distance in middle field to total, %"},
        source="results",
        value_key="distance_center_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    # if there is
    ReportField(
        key="visits_in_1",
        label={"ru": "Пересечение зоны 1", "en": "Zone 1 crossings"},
        source="results",
        value_key="visits_in_1",
        formatter=lambda v: f"{v:.1f}",
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

    ReportField(
        key="visits_in_2",
        label={"ru": "Пересечение зоны 2", "en": "Zone 2 crossings"},
        source="results",
        value_key="visits_in_2",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_in_2",
        label={"ru": "Дистанция в зоне 2, см", "en": "Distance in zone 2, cm"},
        source="results",
        value_key="distance_in_2",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_2",
        label={"ru": "Время в зоне 2, с", "en": "Time in zone 2, s"},
        source="results",
        value_key="time_in_2",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_2",
        label={"ru": "Скорость в зоне 2, см/с", "en": "Speed in zone 2, cm/s"},
        source="results",
        value_key="speed_in_2",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
]
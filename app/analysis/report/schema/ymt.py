from .common import ReportField, COMMON_SCHEMA

YMT_SCHEMA = COMMON_SCHEMA + [
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
        key="distance_Ra",
        label={"ru": "Дисатнция в R1, см", "en": "Distance in R1, cm"},
        source="results",
        value_key="distance_Ra",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_Rb",
        label={"ru": "Дисатнция в R2, см", "en": "Distance in R2, cm"},
        source="results",
        value_key="distance_Rb",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_Rc",
        label={"ru": "Дисатнция в R3, см", "en": "Distance in R3, cm"},
        source="results",
        value_key="distance_Rc",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_center",
        label={"ru": "Дисатнция в центральном поле, см", "en": "Distance in central field, cm"},
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
        key="time_Ra",
        label={"ru": "Время в R1, см", "en": "Time in R1, s"},
        source="results",
        value_key="time_Ra",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_Rb",
        label={"ru": "Время в R2, см", "en": "Time in R2, s"},
        source="results",
        value_key="time_Rb",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_Rc",
        label={"ru": "Время в R3, см", "en": "Time in R3, s"},
        source="results",
        value_key="time_Rc",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_center",
        label={"ru": "Время в центральном поле, см", "en": "Time in central field, s"},
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
        key="transitions_Ra_Rb",
        label={"ru": "Число переходов между R1 и R2 полями, у.е.", "en": "Number of transitions between R1 and R2 fields, units"},
        source="results",
        value_key="transitions_Ra_Rb",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_Ra_Rc",
        label={"ru": "Число переходов между R1 и R3 полями, у.е.", "en": "Number of transitions between R1 and R3 fields, units"},
        source="results",
        value_key="transitions_Ra_Rc",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_Ra_center",
        label={"ru": "Число переходов между R1 и центральным полями, у.е.", "en": "Number of transitions between R1 and central fields, units"},
        source="results",
        value_key="transitions_Ra_center",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_Rb_Rc",
        label={"ru": "Число переходов между R2 и R3 полями, у.е.", "en": "Number of transitions between R2 and R3 fields, units"},
        source="results",
        value_key="transitions_Rb_Rc",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_Rb_center",
        label={"ru": "Число переходов между R2 и центральным полями, у.е.", "en": "Number of transitions between R2 and central fields, units"},
        source="results",
        value_key="transitions_Rb_center",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_Rc_center",
        label={"ru": "Число переходов между R3 и центральным полями, у.е.", "en": "Number of transitions between R3 and central fields, units"},
        source="results",
        value_key="transitions_Rc_center",
        formatter=lambda v: f"{v}",
        default=0
    ),

    # ratio
    ReportField(
        key="time_Ra_ratio",
        label={"ru": "Доля времени в R1 от общего, %", "en": "Proportion of time in R1 to total, %"},
        source="results",
        value_key="time_Ra_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_Rb_ratio",
        label={"ru": "Доля времени в R2 от общего, %", "en": "Proportion of time in R2 to total, %"},
        source="results",
        value_key="time_Rb_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_Rc_ratio",
        label={"ru": "Доля времени в R3 от общего, %", "en": "Proportion of time in R3 to total, %"},
        source="results",
        value_key="time_Rc_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_center_ratio",
        label={"ru": "Доля времени в центральном поле от общего, %", "en": "Proportion of time in central field to total, %"},
        source="results",
        value_key="time_center_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_Ra_ratio",
        label={"ru": "Доля дистанции в R1 от общего, %", "en": "Proportion of distance in R1 to total, %"},
        source="results",
        value_key="distance_Ra_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_Rb_ratio",
        label={"ru": "Доля дистанции в R2 от общего, %", "en": "Proportion of distance in R2 to total, %"},
        source="results",
        value_key="distance_Rb_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_Rc_ratio",
        label={"ru": "Доля дистанции в R3 от общего, %", "en": "Proportion of distance in R3 to total, %"},
        source="results",
        value_key="distance_Rc_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_center_ratio",
        label={"ru": "Доля дистанции в центральном поле от общего, %", "en": "Proportion of distance in central field to total, %"},
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
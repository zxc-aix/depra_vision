from .common import ReportField, COMMON_SCHEMA

CROSS_SCHEMA = COMMON_SCHEMA + [
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
        key="distance_close",
        label={"ru": "Дистанция в закрытых отсеках, см", "en": "Distance in closed compartments, cm"},
        source="results",
        value_key="distance_close",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_open",
        label={"ru": "Дистанция в открытых отсеках, см", "en": "Distance in open compartments, cm"},
        source="results",
        value_key="distance_open",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_center",
        label={"ru": "Дистанция в центальной зоне, см", "en": "Distance in central zone, cm"},
        source="results",
        value_key="distance_center",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_outside",
        label={"ru": "Дистанция вне полей, см, см", "en": "Distance outside fields, cm"},
        source="results",
        value_key="distance_outside",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    # time
    ReportField(
        key="time_close",
        label={"ru": "Время в закрытых отсеках, с", "en": "Time in closed compartments, s"},
        source="results",
        value_key="time_close",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_open",
        label={"ru": "Время в открытых отсеках, с", "en": "Time in open compartments, s"},
        source="results",
        value_key="time_open",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_center",
        label={"ru": "Время в центральной зоне, с", "en": "Time in central zone, s"},
        source="results",
        value_key="time_center",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_outside",
        label={"ru": "Время вне полей, с", "en": "Time outside fields, s"},
        source="results",
        value_key="time_outside",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    # transit
    ReportField(
        key="total_transitions",
        label={"ru": "Число переходов между всеми отсеками, у.е.", "en": "Number of transitions between all compartments, units"},
        source="results",
        value_key="total_transitions",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_open_close",
        label={"ru": "Число переходов между открытым и закрытым отсеками, у.е.", "en": "Number of transitions between open and closed compartments, units"},
        source="results",
        value_key="transitions_open_close",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_open_center",
        label={"ru": "Число переходов между открытым отсеками и центральной зоной, у.е.", "en": "Number of transitions between open compartments and central zone, units"},
        source="results",
        value_key="transitions_open_center",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_open_outside",
        label={"ru": "Число переходов между открытым отсеками и вне поля, у.е.", "en": "Number of transitions between open compartments and outside field, units"},
        source="results",
        value_key="transitions_open_outside",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_center_close",
        label={"ru": "Число переходов между центральной зоной и закрытым отсеками, у.е.", "en": "Number of transitions between central zone and closed compartments, units"},
        source="results",
        value_key="transitions_center_close",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_center_outside",
        label={"ru": "Число переходов между центральной зоной и вне поля, у.е.", "en": "Number of transitions between central zone and outside field, units"},
        source="results",
        value_key="transitions_center_outside",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_close_outside",
        label={"ru": "Число переходов между закрытым отсеками и вне поля у.е.", "en": "Number of transitions between closed compartments and outside field, units"},
        source="results",
        value_key="transitions_close_outside",
        formatter=lambda v: f"{v}",
        default=0
    ),

    # ratio
    ReportField(
        key="distance_close_ratio",
        label={"ru": "Доля дистанции в закрытых отсеках от общей, %", "en": "Proportion of distance in closed compartments to total, %"},
        source="results",
        value_key="distance_close_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_open_ratio",
        label={"ru": "Доля дистанции в открытых отсеках от общей, %", "en": "Proportion of distance in open compartments to total, %"},
        source="results",
        value_key="distance_open_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_center_ratio",
        label={"ru": "Доля дистанции в центальной зоне от общей, %", "en": "Proportion of distance in central zone to total, %"},
        source="results",
        value_key="distance_center_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_close_ratio",
        label={"ru": "Доля времени в закрытых отсеках от общего, %", "en": "Proportion of time in closed compartments to total, %"},
        source="results",
        value_key="time_close_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_open_ratio",
        label={"ru": "Доля времени в открытых отсеках от общего, %", "en": "Proportion of time in open compartments to total, %"},
        source="results",
        value_key="time_open_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_center_ratio",
        label={"ru": "Доля времени в центальной зоне от общего, %", "en": "Proportion of time in central zone to total, %"},
        source="results",
        value_key="time_center_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    # avg
    ReportField(
        key="avg_close_distance",
        label={"ru": "Средняя дистанция в закрытом остеке, см", "en": "Average distance in closed compartment, cm"},
        source="results",
        value_key="avg_close_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_open_distance",
        label={"ru": "Средняя дистанция в окрытом остеке, см", "en": "Average distance in open compartment, cm"},
        source="results",
        value_key="avg_open_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_center_distance",
        label={"ru": "Средняя дистанция в центральной зоне, см", "en": "Average distance in central zone, cm"},
        source="results",
        value_key="avg_center_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_close_time",
        label={"ru": "Среднeе время прибывания в закрытом остеке, с", "en": "Average time spent in closed compartment, s"},
        source="results",
        value_key="avg_close_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_open_time",
        label={"ru": "Среднeе время прибывания в окрытом остеке, с", "en": "Average time spent in open compartment, s"},
        source="results",
        value_key="avg_open_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_center_time",
        label={"ru": "Среднeе время прибывания в центральной зоне, с", "en": "Average time spent in central zone, s"},
        source="results",
        value_key="avg_center_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    
    # speed
    ReportField(
        key="avg_speed",
        label={"ru": "Общая средняя скорость, см/с", "en": "Overall average speed, cm/s"},
        source="results",
        value_key="avg_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_close_speed",
        label={"ru": "Средняя скорость в закрытых отсеках, см/с", "en": "Average speed in closed compartments, cm/s"},
        source="results",
        value_key="avg_close_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_open_speed",
        label={"ru": "Средняя скорость в открытых отсеках, см/с", "en": "Average speed in open compartments, cm/s"},
        source="results",
        value_key="avg_open_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_center_speed",
        label={"ru": "Средняя скорость в центальной зоне, см/с", "en": "Average speed in central zone, cm/s"},
        source="results",
        value_key="avg_center_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_speed_no_freeze",
        label={"ru": "Общая средняя скорость (без учёта остановок), см/с", "en": "Overall average speed (excluding stops), cm/s"},
        source="results",
        value_key="avg_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_close_speed_no_freeze",
        label={"ru": "Средняя скорость в закрытых отсеках (без учёта замираний), см/с", "en": "Average speed in closed compartments (excluding freezes), cm/s"},
        source="results",
        value_key="avg_close_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_open_speed_no_freeze",
        label={"ru": "Средняя скорость в открытых отсеках (без учёта замираний), см/с", "en": "Average speed in open compartments (excluding freezes), cm/s"},
        source="results",
        value_key="avg_open_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_center_speed_no_freeze",
        label={"ru": "Средняя скорость в центальной зоне (без учёта замираний), см/с", "en": "Average speed in central zone (excluding freezes), cm/s"},
        source="results",
        value_key="avg_center_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="max_speed",
        label={"ru": "Максимальная скорость, см/с", "en": "Maximum speed, cm/s"},
        source="results",
        value_key="max_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="min_speed",
        label={"ru": "Минимальная скорость, см/с", "en": "Minimum speed, cm/s"},
        source="results",
        value_key="min_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    # freeze
    ReportField(
        key="freeze_count",
        label={"ru": "Число остановок", "en": "Number of freezes"},
        source="results",
        value_key="freeze_count",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="avg_freeze_time",
        label={"ru": "Среднее время остановок, с", "en": "Average freeze time, s"},
        source="results",
        value_key="avg_freeze_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="freeze_time",
        label={"ru": "Общее время остановок, с", "en": "Total freeze time, s"},
        source="results",
        value_key="freeze_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    # fast/slow
    ReportField(
        key="time_slow",
        label={"ru": "Время, потраченное на медленное движение, с", "en": "Time spent on slow movement, s"},
        source="results",
        value_key="time_slow",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_fast",
        label={"ru": "Время, потраченное на быстрое  движение, с", "en": "Time spent on fast movement, s"},
        source="results",
        value_key="time_fast",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_slow",
        label={"ru": "Дистанция, пройденная медленным движением, см", "en": "Distance traveled by slow movement, cm"},
        source="results",
        value_key="distance_slow",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_fast",
        label={"ru": "Дистанция, пройденная быстрым движением, см", "en": "Distance traveled by fast movement, cm"},
        source="results",
        value_key="distance_fast",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    # added params
    ReportField(
        key="num_defac_acts",
        label={"ru": "Число актов дификаций", "en": "Number of defecation acts"},
        source="manual",
        default=""
    ),
    ReportField(
        key="num_unir_acts",
        label={"ru": "Число актов деуринаций", "en": "Number of urination acts"},
        source="manual",
        default=""
    ),
    ReportField(
        key="risk_pos",
        label={"ru": "Позы оценки риска", "en": "Risk assessment postures"},
        source="manual",
        default=""
    ),
    ReportField(
        key="looking_down",
        label={"ru": "Заглядывания вниз", "en": "Looking down"},
        source="manual",
        default=""
    ),
    ReportField(
        key="num_stand",
        label={"ru": "Число стояний на задних лапах", "en": "Number of rearings"},
        source="manual",
        default=""
    ),
]
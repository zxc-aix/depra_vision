from .common import ReportField, COMMON_SCHEMA

BOX_SCHEMA = COMMON_SCHEMA + [

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
        key="distance_large",
        label={"ru": "Дистанция во внешнем  поле, см", "en": "Distance in outer field, cm"},
        source="results",
        value_key="distance_large",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_medium",
        label={"ru": "Дистанция в среднем поле, см", "en": "Distance in middle field, cm"},
        source="results",
        value_key="distance_medium",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_small",
        label={"ru": "Дистанция во внутреннем поле, см", "en": "Distance in inner field, cm"},
        source="results",
        value_key="distance_small",
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

    # time
    ReportField(
        key="time_large",
        label={"ru": "Время во внешнем  поле, с", "en": "Time in outer field, s"},
        source="results",
        value_key="time_large",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_medium",
        label={"ru": "Время в среднем поле, с", "en": "Time in middle field, s"},
        source="results",
        value_key="time_medium",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_small",
        label={"ru": "Время в внутреннем поле, с", "en": "Time in inner field, s"},
        source="results",
        value_key="time_small",
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
        key="transitions_small_medium",
        label={"ru": "Число переходов между внутреннем и среднем отсеками, у.е.", "en": "Number of transitions between inner and middle compartments, units"},
        source="results",
        value_key="transitions_small_medium",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_small_large",
        label={"ru": "Число переходов между внутреннем и внешнем  отсеками, у.е.", "en": "Number of transitions between inner and outer compartments, units"},
        source="results",
        value_key="transitions_small_large",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_small_outside",
        label={"ru": "Число переходов между внутреннем отсеком и вне поля, у.е.", "en": "Number of transitions between inner compartment and outside field, units"},
        source="results",
        value_key="transitions_small_outside",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_medium_large",
        label={"ru": "Число переходов между среднем и внешнем  отсеками, у.е.", "en": "Number of transitions between middle and outer compartments, units"},
        source="results",
        value_key="transitions_medium_large",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_medium_outside",
        label={"ru": "Число переходов между среднем отсеком и вне поля, у.е.", "en": "Number of transitions between middle compartment and outside field, units"},
        source="results",
        value_key="transitions_medium_outside",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_large_outside",
        label={"ru": "Число переходов между внешнем отсеком и вне поля, у.е.", "en": "Number of transitions between outer compartment and outside field, units"},
        source="results",
        value_key="transitions_large_outside",
        formatter=lambda v: f"{v}",
        default=0
    ),

    # ratio
    ReportField(
        key="distance_large_ratio",
        label={"ru": "Доля дистанции во внешнем поле от общей, %", "en": "Proportion of distance in outer field to total, %"},
        source="results",
        value_key="distance_large_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_medium_ratio",
        label={"ru": "Доля дистанции в среднем поле от общей, %", "en": "Proportion of distance in middle field to total, %"},
        source="results",
        value_key="distance_medium_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_small_ratio",
        label={"ru": "Доля дистанции во внутреннем поле от общей, %", "en": "Proportion of distance in inner field to total, %"},
        source="results",
        value_key="distance_small_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_large_ratio",
        label={"ru": "Доля времени во внешнем поле от общего, %", "en": "Proportion of time in outer field to total, %"},
        source="results",
        value_key="time_large_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_medium_ratio",
        label={"ru": "Доля времени в среднем поле от общего, %", "en": "Proportion of time in middle field to total, %"},
        source="results",
        value_key="time_medium_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_small_ratio",
        label={"ru": "Доля времени во внутреннем поле от общего, %", "en": "Proportion of time in inner field to total, %"},
        source="results",
        value_key="time_small_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    
    # avg
    ReportField(
        key="avg_large_distance",
        label={"ru": "Средняя дистанция во внешнем поле, см", "en": "Average distance in outer field, cm"},
        source="results",
        value_key="avg_large_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_medium_distance",
        label={"ru": "Средняя дистанция в среднем поле, см", "en": "Average distance in middle field, cm"},
        source="results",
        value_key="avg_medium_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_small_distance",
        label={"ru": "Средняя дистанция во внутреннем поле, см", "en": "Average distance in inner field, cm"},
        source="results",
        value_key="avg_small_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_large_time",
        label={"ru": "Среднее время прибывания в внешнем поле, с", "en": "Average time spent in outer field, s"},
        source="results",
        value_key="avg_large_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_medium_time",
        label={"ru": "Среднее время прибывания в среднем поле , с", "en": "Average time spent in middle field, s"},
        source="results",
        value_key="avg_medium_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_small_time",
        label={"ru": "Среднее время прибывания во внутреннем поле, с", "en": "Average time spent in inner field, s"},
        source="results",
        value_key="avg_small_time",
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
        key="avg_large_speed",
        label={"ru": "Средняя скорость во внешнем поле, см/с", "en": "Average speed in outer field, cm/s"},
        source="results",
        value_key="avg_large_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_medium_speed",
        label={"ru": "Средняя скорость в среднем поле, см/с", "en": "Average speed in middle field, cm/s"},
        source="results",
        value_key="avg_medium_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_small_speed",
        label={"ru": "Средняя скорость во внутреннем поле, см/с", "en": "Average speed in inner field, cm/s"},
        source="results",
        value_key="avg_small_speed",
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
        key="avg_large_speed_no_freeze",
        label={"ru": "Средняя скорость во внешнем поле (без учёта остановок), см/с", "en": "Average speed in outer field (excluding stops), cm/s"},
        source="results",
        value_key="avg_large_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_medium_speed_no_freeze",
        label={"ru": "Средняя скорость в среднем поле (без учёта остановок), см/с", "en": "Average speed in middle field (excluding stops), cm/s"},
        source="results",
        value_key="avg_medium_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_small_speed_no_freeze",
        label={"ru": "Средняя скорость во внутреннем поле (без учёта остановок), см/с", "en": "Average speed in inner field (excluding stops), cm/s"},
        source="results",
        value_key="avg_small_speed_no_freeze",
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
        formatter=lambda v: f"{v:.1f}",
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
        key="time_slow_large",
        label={"ru": "Время, потраченное на медленное движение во внешнем поле, с", "en": "Time spent on slow movement in outer field, s"},
        source="results",
        value_key="time_slow_large",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_slow_medium",
        label={"ru": "Время, потраченное на медленное движение в среднем поле, с", "en": "Time spent on slow movement in middle field, s"},
        source="results",
        value_key="time_slow_medium",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_slow_small",
        label={"ru": "Время, потраченное на медленное движение во внутреннем поле, с", "en": "Time spent on slow movement in inner field, s"},
        source="results",
        value_key="time_slow_small",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_fast_small",
        label={"ru": "Время, потраченное на быстрое движение во внешнем поле, с", "en": "Time spent on fast movement in outer field, s"},
        source="results",
        value_key="time_fast_small",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_fast_medium",
        label={"ru": "Время, потраченное на быстрое движение в среднем поле, с", "en": "Time spent on fast movement in middle field, s"},
        source="results",
        value_key="time_fast_medium",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_fast_small",
        label={"ru": "Время, потраченное на быстрое движение во внутреннем поле, с", "en": "Time spent on fast movement in inner field, s"},
        source="results",
        value_key="time_fast_small",
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
    ReportField(
        key="distance_slow_large",
        label={"ru": "Дистанция, пройденная медленным движением в внешнем поле, см", "en": "Distance traveled by slow movement in outer field, cm"},
        source="results",
        value_key="distance_slow_large",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_slow_medium",
        label={"ru": "Дистанция, пройденная медленным движением в среднем поле, см", "en": "Distance traveled by slow movement in middle field, cm"},
        source="results",
        value_key="distance_slow_medium",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_slow_small",
        label={"ru": "Дистанция, пройденная медленным движением в внутреннем поле, см", "en": "Distance traveled by slow movement in inner field, cm"},
        source="results",
        value_key="distance_slow_small",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_fast_small",
        label={"ru": "Дистанция, пройденная быстрым движением в внешнем поле, см", "en": "Distance traveled by fast movement in outer field, cm"},
        source="results",
        value_key="distance_fast_small",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_fast_medium",
        label={"ru": "Дистанция, пройденная быстрым движением в среднем поле, см", "en": "Distance traveled by fast movement in middle field, cm"},
        source="results",
        value_key="distance_fast_medium",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_fast_small",
        label={"ru": "Дистанция, пройденная быстрым движением в внутреннем поле, см", "en": "Distance traveled by fast movement in inner field, cm"},
        source="results",
        value_key="distance_fast_small",
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

    ReportField(
        key="visits_in_3",
        label={"ru": "Пересечение зоны 3", "en": "Zone 3 crossings"},
        source="results",
        value_key="visits_in_3",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_in_3",
        label={"ru": "Дистанция в зоне 3, см", "en": "Distance in zone 3, cm"},
        source="results",
        value_key="distance_in_3",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_3",
        label={"ru": "Время в зоне 3, с", "en": "Time in zone 3, s"},
        source="results",
        value_key="time_in_3",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_3",
        label={"ru": "Скорость в зоне 3, см/с", "en": "Speed in zone 3, cm/s"},
        source="results",
        value_key="speed_in_3",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    ReportField(
        key="visits_in_4",
        label={"ru": "Пересечение зоны 4", "en": "Zone 4 crossings"},
        source="results",
        value_key="visits_in_4",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_in_4",
        label={"ru": "Дистанция в зоне 4, см", "en": "Distance in zone 4, cm"},
        source="results",
        value_key="distance_in_4",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_4",
        label={"ru": "Время в зоне 4, с", "en": "Time in zone 4, s"},
        source="results",
        value_key="time_in_4",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_4",
        label={"ru": "Скорость в зоне 4, см/с", "en": "Speed in zone 4, cm/s"},
        source="results",
        value_key="speed_in_4",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    ReportField(
        key="visits_in_5",
        label={"ru": "Пересечение зоны 5", "en": "Zone 5 crossings"},
        source="results",
        value_key="visits_in_5",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_in_5",
        label={"ru": "Дистанция в зоне 5, см", "en": "Distance in zone 5, cm"},
        source="results",
        value_key="distance_in_5",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_5",
        label={"ru": "Время в зоне 5, с", "en": "Time in zone 5, s"},
        source="results",
        value_key="time_in_5",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_5",
        label={"ru": "Скорость в зоне 5, см/с", "en": "Speed in zone 5, cm/s"},
        source="results",
        value_key="speed_in_5",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    ReportField(
        key="visits_in_6",
        label={"ru": "Пересечение зоны 6", "en": "Zone 6 crossings"},
        source="results",
        value_key="visits_in_6",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_in_6",
        label={"ru": "Дистанция в зоне 6, см", "en": "Distance in zone 6, cm"},
        source="results",
        value_key="distance_in_6",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_6",
        label={"ru": "Время в зоне 6, с", "en": "Time in zone 6, s"},
        source="results",
        value_key="time_in_6",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_6",
        label={"ru": "Скорость в зоне 6, см/с", "en": "Speed in zone 6, cm/s"},
        source="results",
        value_key="speed_in_6",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    ReportField(
        key="visits_in_7",
        label={"ru": "Пересечение зоны 7", "en": "Zone 7 crossings"},
        source="results",
        value_key="visits_in_7",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_in_7",
        label={"ru": "Дистанция в зоне 7, см", "en": "Distance in zone 7, cm"},
        source="results",
        value_key="distance_in_7",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_7",
        label={"ru": "Время в зоне 7, с", "en": "Time in zone 7, s"},
        source="results",
        value_key="time_in_7",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_7",
        label={"ru": "Скорость в зоне 7, см/с", "en": "Speed in zone 7, cm/s"},
        source="results",
        value_key="speed_in_7",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    ReportField(
        key="visits_in_8",
        label={"ru": "Пересечение зоны 8", "en": "Zone 8 crossings"},
        source="results",
        value_key="visits_in_8",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_in_8",
        label={"ru": "Дистанция в зоне 8, см", "en": "Distance in zone 8, cm"},
        source="results",
        value_key="distance_in_8",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_8",
        label={"ru": "Время в зоне 8, с", "en": "Time in zone 8, s"},
        source="results",
        value_key="time_in_8",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_8",
        label={"ru": "Скорость в зоне 8, см/с", "en": "Speed in zone 8, cm/s"},
        source="results",
        value_key="speed_in_8",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    ReportField(
        key="visits_in_9",
        label={"ru": "Пересечение зоны 9", "en": "Zone 9 crossings"},
        source="results",
        value_key="visits_in_9",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_in_9",
        label={"ru": "Дистанция в зоне 9, см", "en": "Distance in zone 9, cm"},
        source="results",
        value_key="distance_in_9",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_9",
        label={"ru": "Время в зоне 9, с", "en": "Time in zone 9, s"},
        source="results",
        value_key="time_in_8",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_9",
        label={"ru": "Скорость в зоне 9, см/с", "en": "Speed in zone 9, cm/s"},
        source="results",
        value_key="speed_in_9",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    ReportField(
        key="visits_in_10",
        label={"ru": "Пересечение зоны 10", "en": "Zone 10 crossings"},
        source="results",
        value_key="visits_in_10",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_in_10",
        label={"ru": "Дистанция в зоне 10, см", "en": "Distance in zone 10, cm"},
        source="results",
        value_key="distance_in_10",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_10",
        label={"ru": "Время в зоне 10, с", "en": "Time in zone 10, s"},
        source="results",
        value_key="time_in_10",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_10",
        label={"ru": "Скорость в зоне 10, см/с", "en": "Speed in zone 10, cm/s"},
        source="results",
        value_key="speed_in_10",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    ReportField(
        key="visits_in_11",
        label={"ru": "Пересечение зоны 11", "en": "Zone 11 crossings"},
        source="results",
        value_key="visits_in_11",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_in_11",
        label={"ru": "Дистанция в зоне 11, см", "en": "Distance in zone 11, cm"},
        source="results",
        value_key="distance_in_11",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_11",
        label={"ru": "Время в зоне 11, с", "en": "Time in zone 11, s"},
        source="results",
        value_key="time_in_11",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_11",
        label={"ru": "Скорость в зоне 11, см/с", "en": "Speed in zone 11, cm/s"},
        source="results",
        value_key="speed_in_11",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    ReportField(
        key="visits_in_12",
        label={"ru": "Пересечение зоны 12", "en": "Zone 12 crossings"},
        source="results",
        value_key="visits_in_12",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_in_12",
        label={"ru": "Дистанция в зоне 12, см", "en": "Distance in zone 12, cm"},
        source="results",
        value_key="distance_in_12",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_12",
        label={"ru": "Время в зоне 12, с", "en": "Time in zone 12, s"},
        source="results",
        value_key="time_in_12",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_12",
        label={"ru": "Скорость в зоне 12, см/с", "en": "Speed in zone 12, cm/s"},
        source="results",
        value_key="speed_in_12",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    ReportField(
        key="visits_in_13",
        label={"ru": "Пересечение зоны 13", "en": "Zone 13 crossings"},
        source="results",
        value_key="visits_in_13",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_in_13",
        label={"ru": "Дистанция в зоне 13, см", "en": "Distance in zone 13, cm"},
        source="results",
        value_key="distance_in_13",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_in_13",
        label={"ru": "Время в зоне 13, с", "en": "Time in zone 13, s"},
        source="results",
        value_key="time_in_13",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="speed_in_13",
        label={"ru": "Скорость в зоне 13, см/с", "en": "Speed in zone 13, cm/s"},
        source="results",
        value_key="speed_in_13",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
]

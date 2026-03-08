from .common import ReportField, COMMON_SCHEMA

MORRIS_SCHEMA = COMMON_SCHEMA + [
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
        key="distance_a_outer",
        label={"ru": "Дистанция в квадранте A, см", "en": "Distance in quadrant A, cm"},
        source="results",
        value_key="distance_a_outer",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_b_outer",
        label={"ru": "Дистанция в квадранте B, см", "en": "Distance in quadrant B, cm"},
        source="results",
        value_key="distance_b_outer",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_c_outer",
        label={"ru": "Дистанция в квадранте C, см", "en": "Distance in quadrant C, cm"},
        source="results",
        value_key="distance_c_outer",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_d_outer",
        label={"ru": "Дистанция в квадранте D, см", "en": "Distance in quadrant D, cm"},
        source="results",
        value_key="distance_d_outer",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_a_inner",
        label={"ru": "Дистанция во внутреннем квадранте A, см", "en": "Distance in inner quadrant A, cm"},
        source="results",
        value_key="distance_a_inner",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_b_inner",
        label={"ru": "Дистанция во внутреннем квадранте B, см", "en": "Distance in inner quadrant B, cm"},
        source="results",
        value_key="distance_b_inner",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_c_inner",
        label={"ru": "Дистанция во внутреннем квадранте C, см", "en": "Distance in inner quadrant C, cm"},
        source="results",
        value_key="distance_c_inner",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_d_inner",
        label={"ru": "Дистанция во внутреннем квадранте D, см", "en": "Distance in inner quadrant D, cm"},
        source="results",
        value_key="distance_d_inner",
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
        key="time_a_outer",
        label={"ru": "Время в квадранте A, см", "en": "Time in quadrant A, cm"},
        source="results",
        value_key="time_a_outer",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_b_outer",
        label={"ru": "Время в квадранте B, см", "en": "Time in quadrant B, cm"},
        source="results",
        value_key="time_b_outer",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_c_outer",
        label={"ru": "Время в квадранте C, см", "en": "Time in quadrant C, cm"},
        source="results",
        value_key="time_c_outer",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_d_outer",
        label={"ru": "Время в квадранте D, см", "en": "Time in quadrant D, cm"},
        source="results",
        value_key="time_d_outer",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_a_inner",
        label={"ru": "Время во внутреннем квадранте A, см", "en": "Time in inner quadrant A, cm"},
        source="results",
        value_key="time_a_inner",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_b_inner",
        label={"ru": "Время во внутреннем квадранте B, см", "en": "Time in inner quadrant B, cm"},
        source="results",
        value_key="time_b_inner",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_c_inner",
        label={"ru": "Время во внутреннем квадранте C, см", "en": "Time in inner quadrant C, cm"},
        source="results",
        value_key="time_c_inner",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_d_inner",
        label={"ru": "Время во внутреннем квадранте D, см", "en": "Time in inner quadrant D, cm"},
        source="results",
        value_key="time_d_inner",
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
        key="transitions_a_outer_b_outer",
        label={"ru": "Число переходов между квадрантом А и B, у.е.", "en": "Number of transitions between quadrant A and B, units"},
        source="results",
        value_key="transitions_a_outer_b_outer",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_a_outer_c_outer",
        label={"ru": "Число переходов между квадрантом A и C, у.е.", "en": "Number of transitions between quadrant A and C, units"},
        source="results",
        value_key="transitions_a_outer_c_outer",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_a_outer_d_outer",
        label={"ru": "Число переходов между квадрантом A и D, у.е.", "en": "Number of transitions between quadrant A and D, units"},
        source="results",
        value_key="transitions_a_outer_d_outer",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_b_outer_c_outer",
        label={"ru": "Число переходов между квадрантом B и C, у.е.", "en": "Number of transitions between quadrant B and C, units"},
        source="results",
        value_key="transitions_b_outer_c_outer",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_b_outer_d_outer",
        label={"ru": "Число переходов между квадрантом B и D, у.е.", "en": "Number of transitions between quadrant B and D, units"},
        source="results",
        value_key="transitions_b_outer_d_outer",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_c_outer_d_outer",
        label={"ru": "Число переходов между квадрантом C и D, у.е.", "en": "Number of transitions between quadrant C and D, units"},
        source="results",
        value_key="transitions_c_outer_d_outer",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_a_inner_b_inner",
        label={"ru": "Число переходов между внутренними квадрантом А и B, у.е.", "en": "Number of transitions between inner quadrant A and B, units"},
        source="results",
        value_key="transitions_a_inner_b_inner",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_a_inner_c_inner",
        label={"ru": "Число переходов между внутренними квадрантом A и C, у.е.", "en": "Number of transitions between inner quadrant A and C, units"},
        source="results",
        value_key="transitions_a_inner_c_inner",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_a_inner_d_inner",
        label={"ru": "Число переходов между внутренними квадрантом A и D, у.е.", "en": "Number of transitions between inner quadrant A and D, units"},
        source="results",
        value_key="transitions_a_inner_d_inner",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_b_inner_c_inner",
        label={"ru": "Число переходов между внутренними квадрантом B и C, у.е.", "en": "Number of transitions between inner quadrant B and C, units"},
        source="results",
        value_key="transitions_b_inner_c_inner",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_b_inner_d_inner",
        label={"ru": "Число переходов между внутренними квадрантом B и D, у.е.", "en": "Number of transitions between inner quadrant B and D, units"},
        source="results",
        value_key="transitions_b_inner_d_inner",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_c_inner_d_inner",
        label={"ru": "Число переходов между внутренними квадрантом C и D, у.е.", "en": "Number of transitions between inner quadrant C and D, units"},
        source="results",
        value_key="transitions_c_inner_d_inner",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_a_inner_a_outer",
        label={"ru": "Число переходов между внешним и внутренним A, у.е.", "en": "Number of transitions between outer and inner A, units"},
        source="results",
        value_key="transitions_a_inner_a_outer",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_b_inner_b_outer",
        label={"ru": "Число переходов между внешним и внутренним B, у.е.", "en": "Number of transitions between outer and inner B, units"},
        source="results",
        value_key="transitions_b_inner_b_outer",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_c_inner_c_outer",
        label={"ru": "Число переходов между внешним и внутренним C, у.е.", "en": "Number of transitions between outer and inner C, units"},
        source="results",
        value_key="transitions_c_inner_c_outer",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="transitions_d_inner_d_outer",
        label={"ru": "Число переходов между внешним и внутренним D, у.е.", "en": "Number of transitions between outer and inner D, units"},
        source="results",
        value_key="transitions_d_inner_d_outer",
        formatter=lambda v: f"{v}",
        default=0
    ),

    # ratio
    ReportField(
        key="distance_a_outer_ratio",
        label={"ru": "Доля дистанции в квадранте A от вcей дистанции, %", "en": "Proportion of distance in quadrant A to total distance, %"},
        source="results",
        value_key="distance_a_outer_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_b_outer_ratio",
        label={"ru": "Доля дистанции в квадранте B от вcей дистанции, %", "en": "Proportion of distance in quadrant B to total distance, %"},
        source="results",
        value_key="distance_b_outer_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_c_outer_ratio",
        label={"ru": "Доля дистанции в квадранте C от вcей дистанции, %", "en": "Proportion of distance in quadrant C to total distance, %"},
        source="results",
        value_key="distance_c_outer_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_d_outer_ratio",
        label={"ru": "Доля дистанции в квадранте D от вcей дистанции, %", "en": "Proportion of distance in quadrant D to total distance, %"},
        source="results",
        value_key="distance_d_outer_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_a_outer_ratio",
        label={"ru": "Доля времени в квадранте A от вcей дистанции, %", "en": "Proportion of time in quadrant A to total distance, %"},
        source="results",
        value_key="time_a_outer_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_b_outer_ratio",
        label={"ru": "Доля времени в квадранте B от вcей дистанции, %", "en": "Proportion of time in quadrant B to total distance, %"},
        source="results",
        value_key="time_b_outer_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_c_outer_ratio",
        label={"ru": "Доля времени в квадранте C от вcей дистанции, %", "en": "Proportion of time in quadrant C to total distance, %"},
        source="results",
        value_key="time_c_outer_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_d_outer_ratio",
        label={"ru": "Доля времени в квадранте D от вcей дистанции, %", "en": "Proportion of time in quadrant D to total distance, %"},
        source="results",
        value_key="time_d_outer_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_a_inner_ratio",
        label={"ru": "Доля дистанции во внутреннем квадранте A от вcей дистанции, %", "en": "Proportion of distance in inner quadrant A to total distance, %"},
        source="results",
        value_key="distance_a_inner_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_b_inner_ratio",
        label={"ru": "Доля дистанции во внутреннем квадранте B от вcей дистанции, %", "en": "Proportion of distance in inner quadrant B to total distance, %"},
        source="results",
        value_key="distance_b_inner_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_c_inner_ratio",
        label={"ru": "Доля дистанции во внутреннем квадранте C от вcей дистанции, %", "en": "Proportion of distance in inner quadrant C to total distance, %"},
        source="results",
        value_key="distance_c_inner_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="distance_d_inner_ratio",
        label={"ru": "Доля дистанции во внутреннем квадранте D от вcей дистанции, %", "en": "Proportion of distance in inner quadrant D to total distance, %"},
        source="results",
        value_key="distance_d_inner_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_a_inner_ratio",
        label={"ru": "Доля времени во внутреннем квадранте A от вcей дистанции, %", "en": "Proportion of time in inner quadrant A to total distance, %"},
        source="results",
        value_key="time_a_inner_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_b_inner_ratio",
        label={"ru": "Доля времени во внутреннем квадранте B от вcей дистанции, %", "en": "Proportion of time in inner quadrant B to total distance, %"},
        source="results",
        value_key="time_b_inner_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_c_inner_ratio",
        label={"ru": "Доля времени во внутреннем квадранте C от вcей дистанции, %", "en": "Proportion of time in inner quadrant C to total distance, %"},
        source="results",
        value_key="time_c_inner_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="time_d_inner_ratio",
        label={"ru": "Доля времени во внутреннем квадранте D от вcей дистанции, %", "en": "Proportion of time in inner quadrant D to total distance, %"},
        source="results",
        value_key="time_d_inner_ratio",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    # avg
    ReportField(
        key="avg_a_outer_distance",
        label={"ru": "Средняя дистанция в квадранте A, см", "en": "Average distance in quadrant A, cm"},
        source="results",
        value_key="avg_a_outer_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_b_outer_distance",
        label={"ru": "Средняя дистанция в квадранте B, см", "en": "Average distance in quadrant B, cm"},
        source="results",
        value_key="avg_b_outer_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_c_outer_distance",
        label={"ru": "Средняя дистанция в квадранте C, см", "en": "Average distance in quadrant C, cm"},
        source="results",
        value_key="avg_c_outer_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_d_outer_distance",
        label={"ru": "Средняя дистанция в квадранте D, см", "en": "Average distance in quadrant D, cm"},
        source="results",
        value_key="avg_d_outer_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_a_outer_time",
        label={"ru": "Среднее время в квадранте A, см", "en": "Average time in quadrant A, cm"},
        source="results",
        value_key="avg_a_outer_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_b_outer_time",
        label={"ru": "Среднее время в квадранте B, см", "en": "Average time in quadrant B, cm"},
        source="results",
        value_key="avg_b_outer_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_c_outer_time",
        label={"ru": "Среднее время в квадранте C, см", "en": "Average time in quadrant C, cm"},
        source="results",
        value_key="avg_c_outer_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_d_outer_time",
        label={"ru": "Среднее время в квадранте D, см", "en": "Average time in quadrant D, cm"},
        source="results",
        value_key="avg_d_outer_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_a_inner_distance",
        label={"ru": "Средняя дистанция во внутреннем квадранте A, см", "en": "Average distance in inner quadrant A, cm"},
        source="results",
        value_key="avg_a_inner_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_b_inner_distance",
        label={"ru": "Средняя дистанция во внутреннем квадранте B, см", "en": "Average distance in inner quadrant B, cm"},
        source="results",
        value_key="avg_b_inner_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_c_inner_distance",
        label={"ru": "Средняя дистанция во внутреннем квадранте C, см", "en": "Average distance in inner quadrant C, cm"},
        source="results",
        value_key="avg_c_inner_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_d_inner_distance",
        label={"ru": "Средняя дистанция во внутреннем квадранте D, см", "en": "Average distance in inner quadrant D, cm"},
        source="results",
        value_key="avg_d_inner_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_a_inner_time",
        label={"ru": "Среднее время во внутреннем квадрантеA, см", "en": "Average time in inner quadrant A, cm"},
        source="results",
        value_key="avg_a_inner_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_b_inner_time",
        label={"ru": "Среднее время во внутреннем квадранте B, см", "en": "Average time in inner quadrant B, cm"},
        source="results",
        value_key="avg_b_inner_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_c_inner_time",
        label={"ru": "Среднее время во внутреннем квадранте C, см", "en": "Average time in inner quadrant C, cm"},
        source="results",
        value_key="avg_c_inner_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_d_inner_time",
        label={"ru": "Среднее время во внутреннем квадранте D, см", "en": "Average time in inner quadrant D, cm"},
        source="results",
        value_key="avg_d_inner_time",
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
        key="avg_speed_no_freeze",
        label={"ru": "Общая средняя скорость (без учёта остановок), см/с", "en": "Overall average speed (excluding stops), cm/s"},
        source="results",
        value_key="avg_speed_no_freeze",
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
    ReportField(
        key="avg_a_outer_speed",
        label={"ru": "Средняя скорость в квадранте A, см/с", "en": "Average speed in quadrant A, cm/s"},
        source="results",
        value_key="avg_a_outer_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_b_outer_speed",
        label={"ru": "Средняя скорость в квадранте B, см/с", "en": "Average speed in quadrant B, cm/s"},
        source="results",
        value_key="avg_b_outer_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_c_outer_speed",
        label={"ru": "Средняя скорость в квадранте C, см/с", "en": "Average speed in quadrant C, cm/s"},
        source="results",
        value_key="avg_c_outer_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_d_outer_speed",
        label={"ru": "Средняя скорость в квадранте D, см/с", "en": "Average speed in quadrant D, cm/s"},
        source="results",
        value_key="avg_d_outer_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_a_outer_speed_no_freeze",
        label={"ru": "Средняя скорость в квадранте A (без учёта остановок), см/с", "en": "Average speed in quadrant A (excluding stops), cm/s"},
        source="results",
        value_key="avg_a_outer_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_b_outer_speed_no_freeze",
        label={"ru": "Средняя скорость в квадранте B (без учёта остановок), см/с", "en": "Average speed in quadrant B (excluding stops), cm/s"},
        source="results",
        value_key="avg_b_outer_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_c_outer_speed_no_freeze",
        label={"ru": "Средняя скорость в квадранте C (без учёта остановок), см/с", "en": "Average speed in quadrant C (excluding stops), cm/s"},
        source="results",
        value_key="avg_c_outer_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_d_outer_speed_no_freeze",
        label={"ru": "Средняя скорость в квадранте D (без учёта остановок), см/с", "en": "Average speed in quadrant D (excluding stops), cm/s"},
        source="results",
        value_key="avg_d_outer_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_a_inner_speed",
        label={"ru": "Средняя скорость во внутреннем квадранте A, см/с", "en": "Average speed in inner quadrant A, cm/s"},
        source="results",
        value_key="avg_a_inner_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_b_inner_speed",
        label={"ru": "Средняя скорость во внутреннем квадранте B, см/с", "en": "Average speed in inner quadrant B, cm/s"},
        source="results",
        value_key="avg_b_inner_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_c_inner_speed",
        label={"ru": "Средняя скорость во внутреннем квадранте C, см/с", "en": "Average speed in inner quadrant C, cm/s"},
        source="results",
        value_key="avg_c_inner_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_d_inner_speed",
        label={"ru": "Средняя скорость во внутреннем квадранте D, см/с", "en": "Average speed in inner quadrant D, cm/s"},
        source="results",
        value_key="avg_d_inner_speed",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_a_inner_speed_no_freeze",
        label={"ru": "Средняя скорость во внутреннем квадранте A (без учёта остановок), см/с", "en": "Average speed in inner quadrant A (excluding stops), cm/s"},
        source="results",
        value_key="avg_a_inner_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_b_inner_speed_no_freeze",
        label={"ru": "Средняя скорость во внутреннем квадранте B (без учёта остановок), см/с", "en": "Average speed in inner quadrant B (excluding stops), cm/s"},
        source="results",
        value_key="avg_b_inner_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_c_inner_speed_no_freeze",
        label={"ru": "Средняя скорость во внутреннем квадранте C (без учёта остановок), см/с", "en": "Average speed in inner quadrant C (excluding stops), cm/s"},
        source="results",
        value_key="avg_c_inner_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="avg_d_inner_speed_no_freeze",
        label={"ru": "Средняя скорость во внутреннем квадранте D (без учёта остановок), см/с", "en": "Average speed in inner quadrant D (excluding stops), cm/s"},
        source="results",
        value_key="avg_d_inner_speed_no_freeze",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),

    # freeze
    ReportField(
        key="freeze_count",
        label={"ru": "Число замираний, у.е.", "en": "Number of freezes, units"},
        source="results",
        value_key="freeze_count",
        formatter=lambda v: f"{v}",
        default=0
    ),
    ReportField(
        key="avg_freeze_time",
        label={"ru": "Среднее время замираний, с", "en": "Average freeze time, s"},
        source="results",
        value_key="avg_freeze_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="freeze_time",
        label={"ru": "Общее время замираний, с", "en": "Total freeze time, s"},
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

    # eval teach
    ReportField(
        key="baseline_gallagher",
        label={"ru": "Средняя близость к платформе (близость Галлахера), классическая", "en": "Average proximity to platform (Gallagher proximity), classical"},
        source="results",
        value_key="baseline_gallagher",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="adjusted_gallagher",
        label={"ru": "Средняя близость к платформе (близость Галлахера), вне платформы", "en": "Average proximity to platform (Gallagher proximity), off-platform"},
        source="results",
        value_key="adjusted_gallagher",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="composite_gallagher",
        label={"ru": "Средняя близость к платформе (близость Галлахера), взвешенное среднее", "en": "Average proximity to platform (Gallagher proximity), weighted average"},
        source="results",
        value_key="composite_gallagher",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="cumulative_error",
        label={"ru": "Кумулятивная ошибка поиска", "en": "Cumulative search error"},
        source="results",
        value_key="cumulative_error",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="whishow_error",
        label={"ru": "Ошибка Уишоу", "en": "Whishaw error"},
        source="results",
        value_key="whishow_error",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="angle_error_after_distance",
        label={"ru": "Ошибка углового направления (по дистанции)", "en": "Angular direction error (by distance)"},
        source="results",
        value_key="angle_error_after_distance",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="angle_error_after_time",
        label={"ru": "Ошибка углового направления (по времени)", "en": "Angular direction error (by time)"},
        source="results",
        value_key="angle_error_after_time",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="angle_error_after_percent",
        label={"ru": "Ошибка углового направления (в процентах по дистанции)", "en": "Angular direction error (percentage by distance)"},
        source="results",
        value_key="angle_error_after_percent",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="escape_latency",
        label={"ru": "Время поиска платформы (латентное время, время задержки), с", "en": "Platform search time (escape latency), s"},
        source="results",
        value_key="escape_latency",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="on_platform",
        label={"ru": "Количество пересечений зоны платформы (общее)", "en": "Number of platform zone crossings (total)"},
        source="results",
        value_key="on_platform",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="zone_0",
        label={"ru": "Количество пересечений зоны 1", "en": "Number of zone 1 crossings"},
        source="results",
        value_key="zone_0",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="zone_1",
        label={"ru": "Количество пересечений зоны 2", "en": "Number of zone 2 crossings"},
        source="results",
        value_key="zone_1",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="zone_2",
        label={"ru": "Количество пересечений зоны 3", "en": "Number of zone 3 crossings"},
        source="results",
        value_key="zone_2",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="zone_3",
        label={"ru": "Количество пересечений зоны 4", "en": "Number of zone 4 crossings"},
        source="results",
        value_key="zone_3",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="zone_4",
        label={"ru": "Количество пересечений зоны 5", "en": "Number of zone 5 crossings"},
        source="results",
        value_key="zone_4",
        formatter=lambda v: f"{v:.1f}",
        default=0
    ),
    ReportField(
        key="zone_5",
        label={"ru": "Количество пересечений зоны 6", "en": "Number of zone 6 crossings"},
        source="results",
        value_key="zone_5",
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
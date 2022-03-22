def study_schedule(permanence_period, target_time):
    accumulator_students_in_target_time = 0
    try:
        for start_time, end_time in permanence_period:
            if start_time <= target_time <= end_time:
                accumulator_students_in_target_time += 1
        return accumulator_students_in_target_time
    except TypeError:
        return None
# Para ir sendo "somado/acumulado" o accumulator_students_in_target_time,
# o target time, tem que estar entre o start_time e o end time.
# Será retornado None, conforme solicitado no requisito,
# se forem passados argumentos do tipo não apropriado.

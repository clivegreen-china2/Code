def settings() -> dict:
    first_peak_hour: int = 8
    last_peak_hour: int = 15
    final_hour: int = 23
    min_duration: int = 1
    discounts: dict[str:float] = dict(peak=0.1, off_peak=0.5)
    day_property_names: [str] = [
        'peak_max_hours',
        'peak_price',
        'off_peak_price'
    ]
    day_data: [[float]] = [
        [8.0, 02.00, 02.00],
        [2.0, 10.00, 02.00],
        [2.0, 10.00, 02.00],
        [2.0, 10.00, 02.00],
        [2.0, 10.00, 02.00],
        [2.0, 10.00, 02.00],
        [4.0, 03.00, 02.00]
    ]
    day_settings: dict[str:dict[str:float]] = {}
    for index, row in enumerate(day_data):
        day_number = index + 1
        settings_for_day = dict(zip(day_property_names, row))
        day_settings.update({str(day_number): settings_for_day})

    valid_days = list(day_settings.keys())

    hours = dict(
        first_peak_hour=first_peak_hour,
        last_peak_hour=last_peak_hour,
        final_hour=final_hour,
        min_duration=min_duration,
        all_hours=list(range(first_peak_hour, final_hour+1)),
        peak_hours=list(range(first_peak_hour, last_peak_hour)),
        off_peak_hours=list(range(last_peak_hour, final_hour+1))
    )

    return dict(
        discounts=discounts,
        day_settings=day_settings,
        valid_days=valid_days,
        hours=hours
    )

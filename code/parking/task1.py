import sys
import settings
from fpn import fpn_is_valid


settings = settings.settings()
day_settings: dict[int:[float]] = settings['day_settings']
parking_days: [int] = settings['valid_days']
parking_hours: [int] = settings['hours']['all_hours']


def calculate_price(day: str, hour: int, duration: float, fpn: str | None) -> float:

    if day not in parking_days:
        print('invalid day (enter 1 to 7)')
        sys.exit()

    if hour not in parking_hours:
        print('invalid hour (enter 8 to 23')
        sys.exit()

    settings_for_day = day_settings[day]

    # determine minimum and maximum parking durations:
    min_duration: int = settings['hours']['min_duration']

    is_peak: bool = False
    if hour in settings['hours']['peak_hours']:
        is_peak = True
        max_duration = settings_for_day['peak_max_hours']
    else:
        max_duration = settings['hours']['final_hour'] - hour + 1

    if duration < min_duration:
        print(f'duration is too short (min. is {min_duration})')
        sys.exit()

    elif duration > max_duration:
        print(f'duration is too long (max. is {max_duration})')
        sys.exit()

    scale_factor: float = 1.0
    if fpn_is_valid(fpn):
        discounts = settings['discounts']
        if is_peak:
            discount = discounts['peak']
        else:
            discount = discounts['off_peak']
        scale_factor = 1.0 - discount

    prefix = '' if is_peak else 'off_'
    price = settings_for_day[f'{prefix}peak_price']
    total_cost = scale_factor * duration * price
    return total_cost

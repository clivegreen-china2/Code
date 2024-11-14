from datetime import time
from fpn import generate_fpn
from task1 import calculate_price

day_names = [
    '--',
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]

day, hour, duration = '6', 18, 5
fpn: str = generate_fpn()
the_price: float = calculate_price(day, hour, duration, fpn)

day_name = day_names[int(day)]
time = time(hour).strftime('%H:%M')
print(
    f'{day_name} at {time} for {duration} hours: ${the_price:.2f}.'
)

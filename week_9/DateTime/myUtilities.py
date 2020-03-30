import numpy as np
from datetime import date, datetime, timedelta, time

def get_meeting_dates(period_as_timedelta, time_of_day, number_of_meetings, start_date=date.today()):
    if number_of_meetings > period_as_timedelta.days:
        raise ValueError('Too many meetings!...')

    day_deltas = np.linspace(0, period_as_timedelta.days - 1, number_of_meetings, dtype=int)
    base_time_of_day = datetime.combine(start_date, time_of_day)
    list_of_meetings = [base_time_of_day + timedelta(int(day_delta)) for day_delta in day_deltas]
    return list_of_meetings

meetings = get_meeting_dates(timedelta(700), time(17, 0), 1)
print(meetings)
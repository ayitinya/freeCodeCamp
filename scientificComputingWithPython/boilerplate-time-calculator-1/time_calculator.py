def add_time(start, duration, day=str()):

    no_of_days = int()

    days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_dict = {
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6,
        'sunday': 7
    }

    if day:
        day = day.lower()
        day = days_dict[day]

    start = start.split()
    time, session = start
    time = time.split(':')
    hours, minutes = time
    hours = int(hours)
    minutes = int(minutes)

    if session == 'PM':
        if str(hours) != '12':
            hours += 12

    if session == 'AM':
        if hours == 12:
            hours = 0

    duration = duration.split(':')
    hours_duration, minutes_duration = duration
    hours_duration = int(hours_duration)
    minutes_duration = int(minutes_duration)

    new_hour = hours + hours_duration
    new_minutes = minutes + minutes_duration

    if new_minutes >= 60:
        add_hour = new_minutes // 60
        new_minutes = new_minutes % 60
        new_hour += add_hour

    else:
        pass

    if new_minutes > 10:
        pass
    else:
        new_minutes = str(new_minutes)
        new_minutes = '0' + new_minutes

    if new_hour >= 24:
        no_of_days = new_hour//24
        new_hour = new_hour % 24
        if no_of_days > 0:

            if new_hour < 12:
                session = 'AM'
                if new_hour == 0:
                    new_hour = 12

            elif new_hour == 12:
                session = 'PM'
            else:
                new_hour -= 12
                session = 'PM'

            if no_of_days == 1:
                text = 'next day'
            else:
                text = f'{no_of_days} days later'

        if day:
            day = day + no_of_days
            if day > 7:
                day = day % 7
                day_name = days_list[day - 1]
            else:
                day_name = days_list[day - 1]

    else:
        if new_hour > 12:
            new_hour -= 12
            session = 'PM'
        elif new_hour == 12:
            session = 'PM'
        elif new_hour == 0:
            session = 'AM'
            new_hour = 12

        if day:
            day_name = days_list[day - 1]

    if no_of_days:
        if day:
            return f'{new_hour}:{new_minutes} {session}, {day_name} ({text})'
        else:
            return f'{new_hour}:{new_minutes} {session} ({text})'
    else:
        if day:
            return f'{new_hour}:{new_minutes} {session}, {day_name}'
        else:
            return f'{new_hour}:{new_minutes} {session}'


if __name__ == '__main__':
    print(add_time("11:55 AM", "3:12"))

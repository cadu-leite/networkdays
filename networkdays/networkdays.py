import datetime


def networkdays(date_start, date_end, holidays=set(), weekdaysoff={6,7}):
    '''
    NetWorkDays like Excel Networkdays function.

    Args:
        date_start (datetime.date): initial date
        date_end (datetime.date): if none, is the last day of the date_start year.
        workdays (set): set (list) of workin days in iso format, Monday is 1 and Sunday is 7.
        holidays (set): datetime object set, indicating days off.
        weekdaysoff (set): set of weekdays not working, default is saturday and sunday {6,7}.

    returns:
        set of work days.

    ex.:

    '''
    if len(weekdaysoff) == 0:
        weekdaysoff = {6, 7}

    date_diff = date_end-date_start
    workdays = {
        date_start + datetime.timedelta(days=days)
        for days in range(0, (date_diff.days+1))
        if (date_start + datetime.timedelta(days=days)).isoweekday()
        not in weekdaysoff
    }

    workdays = workdays.difference(holidays)

    return workdays


def workdays(duration, workhours, date_start):
    '''
    list workdays given a number of hours distributed in workdays.

    Args:
        duration (int/decimal): job duratin on hours
        workhours (int/decimal):
        date_start

    Returns:
        set: workday datetime.date list
    '''
    workdays_number = duration / workhours
    r = duration % workhours
    if r != 0:
        workdays_number += 1

    delta = datetime.timedelta(days=workdays_number)
    date_end = date_start + delta
    workdays = networkdays(date_start, date_end)

    return workdays

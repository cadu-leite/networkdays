import datetime


class Networkdays:

    def __init__(self, date_start, date_end=None, holidays=set(), weekdaysoff={6,7}):
        self.date_start = date_start
        self.date_end = date_end
        self.holidays = holidays
        self.weekdaysoff = weekdaysoff

    def networkdays(self):
        '''
        NetWorkDays like Excel Networkdays function.
        given 2 dates, the return will the number of days bewteen dates, minus
        hoilidays, e week days off (ex.: saturday and sunday).

        The `weekdaysoff` is a per week iso days list where Monday is 1 and sunday is 7.
        The holidays may be any single date, datetime.date object, in a year.

        Args:
            date_start (datetime.date): initial date
            date_end (datetime.date): end date, or if none, is the last day of the
                date_start year.
            workdays (set): set (list) of workin days in iso format,
                Monday is 1 and Sunday is 7.
            holidays (set): datetime object set, indicating days off.
            weekdaysoff (set): set of weekdays not working,
                default is saturday and sunday {6,7}.

        returns:
            list of work days.

        ex.:
            networkdays(
                datetime.date(2020,1,1),
                datetime.date(2020,2,31),
                holiday=datetime.date(2020,1,1),
                weekdaysoff={6,7}
            )


        '''

        date_diff = self.date_end - self.date_start
        workdays = {
            self.date_start + datetime.timedelta(days=days)
            for days in range(0, (date_diff.days+1))
            if (self.date_start + datetime.timedelta(days=days)).isoweekday()
            not in self.weekdaysoff
        }

        workdays = workdays.difference(self.holidays)
        workdays = sorted(workdays)

        return workdays


class JobSchedule:

    def __init__(self, duration, workhours, date_start, networkdays=None):
        '''
         Args:
            duration (int/decimal): job duratin on hours
            workhours (int/decimal):
            date_start: a base date to start count
            networkdays: a Networkdays instance.

        '''
        self.duration = duration
        self.date_start = date_start
        self.workhours = workhours
        self.networkdays = networkdays

    def job_workdays(self):
        '''
        list workdays for a given job duration

        Returns:
            list: workday datetime.date list
        '''
        # number of workdays based on daily hours
        workdays_number = int(self.duration // self.workhours)
        r = self.duration % self.workhours
        # check if need a partial day of work
        if r != 0:
            workdays_number += 1

        if self.networkdays is None:
            delta = datetime.timedelta(days=workdays_number)
            date_end = self.date_start + delta
            self.networkdays = Networkdays(self.date_start, date_end)\

        workdays = self.networkdays.networkdays()

        # job schedule starts on date_start of the job
        # look for the closest date  of date_start to start the job
        while True:
            try:
                first_day_job = workdays.index(self.date_start)
                break
            except ValueError:
                self.date_start += datetime.timedelta(days=1)

        if workdays_number < len(workdays):
            # only workdays and not the entire calendar
            # todo: set a "borrow" flag, when last workday > date_end
            workdays = workdays[first_day_job:first_day_job+workdays_number]

        return workdays



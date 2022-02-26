from calendar import SATURDAY, SUNDAY
import datetime
from itertools import groupby


class Networkdays:

    def __init__(self, date_start, date_end=None, holidays=set(), weekdaysoff={SATURDAY, SUNDAY}):
        self.date_start = date_start
        self.date_end = self.valid_date_end(date_end)
        self.holidays_set = holidays
        self.weekdaysoff = weekdaysoff

    def valid_date_end(self, date_end):
        if not date_end:
            date_end = self.date_start.replace(
                year=self.date_start.year + 1
            )
        return date_end

    def dates_range(self):
        date_diff = self.date_end - self.date_start
        dates = {
            self.date_start + datetime.timedelta(days=days)
            for days in range(date_diff.days + 1)
        }
        return dates

    def networkdays(self):
        '''
        NetWorkDays is like the Excel function Networkdays.
        Given 2 dates, the return will be the number of days between the dates,
        minus the holidays and days off for the week (ex.: saturday and sunday).

        The holidays can be any date, a datetime.date object, in a year.

        Args:
            date_start (datetime.date): initial date
            date_end (datetime.date): end date, or if none, is the last day of the
                date_start year.
            workdays (set): set (list) of working days in ISO format,
                Monday is 0 and Sunday is 6.
            holidays (set): datetime object set, indicating days off.
            weekdaysoff (set): set of weekdays not working,
                default is Saturday and Sunday {5, 6}.

        returns:
            list of work days.

        usage ex.:
            networkdays(
                datetime.date(2020,1,1),
                datetime.date(2020,2,31),
                holiday=datetime.date(2020,1,1),
                weekdaysoff={5, 6}
            )

        '''
        dates = self.dates_range()
        dates.difference_update(self.weekends(), self.holidays())
        return dates

    def is_date_weekend(self, date) -> bool:
        return date.weekday() in self.weekdaysoff

    def weekends(self):
        dates = self.dates_range()
        dates = filter(self.is_date_weekend, dates)
        return sorted(dates)

    def is_date_included(self, date) -> bool:
        return self.date_end >= date >= self.date_start

    def holidays(self):
        l = filter(self.is_date_included, self.holidays_set)
        return sorted(l)


class JobSchedule:

    def __init__(self, project_duration_hours, workhours_per_day, date_start, networkdays=None):
        '''
         Args:
            project_duration_hours (int/decimal): job duration on hours
            workhours_per_day (int/decimal):
            date_start: a base date to start count
            networkdays: a Networkdays instance.

        '''
        self.project_duration_hours = project_duration_hours
        self.date_start = date_start
        self.workhours_per_day = workhours_per_day
        self.networkdays = networkdays

        self.jobdays = self.job_workdays()

        self.bussines_days = len(self.jobdays)
        self.total_days = self.jobdays[-1] - self.jobdays[0]
        self.prj_starts = self.jobdays[0].strftime('%x')  # todo: localization
        self.prj_ends = self.jobdays[-1].strftime('%x')  # set location

    def job_workdays(self):
        '''
        list workdays for a given job duration

        Returns:
            list: workday datetime.date list
        '''
        # number of workdays based on daily hours
        workdays_number = int(self.project_duration_hours // self.workhours_per_day)
        r = self.project_duration_hours % self.workhours_per_day
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
            workdays = workdays[first_day_job:first_day_job + workdays_number]

        return workdays

    def years(self):
        '''
        Its not duration
        '''
        return iter(range(
            self.jobdays[0].year,
            self.jobdays[-1].year + 1
        ))

    def months(self, year=None):
        """return a weeks `iterATOR`

        Args:
            year (None, optional): Description

        Returns:
            TYPE: Description
        """
        days = self.jobdays
        if year:
            days = filter(lambda x: x.year == year, days)
        return iter([year for year, days_per_year in groupby(days, lambda x: x.month)])

    def weeks(self, year=None, month=None):
        """
        return an `interator`
        for ISO format see
        https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar)

        Args:
            year (None, optional): filter per year
            month (None, optional): filter per month

        Returns:
            iter: weeks iso numbers based
        """
        days = self.jobdays
        if year:
            days = filter(lambda x: x.year == year, days)
        if month:
            days = filter(lambda x: x.month == month, days)

        return iter([weeks for weeks, days_per_year in groupby(days, lambda x: x.isocalendar()[1])])

    def days(self):
        return iter(self.jobdays)

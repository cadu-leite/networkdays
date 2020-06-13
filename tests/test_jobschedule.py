import unittest
import datetime

from networkdays.networkdays import JobSchedule, Networkdays


class TestClassJobSchedule(unittest.TestCase):

    def test_job_workdays(self):
        '''
        November 2020
        Mo Tu We Th Fr Sa Su
                           1
         2  3  4  5  6  7  8
         9 10 11 12 13 14 15
        16 17 18 19 20 21 22
        23 24 25 26 27 28 29
        30
        '''
        jobworkday = JobSchedule(8, 8, datetime.date(2020, 11, 1))
        days = jobworkday.job_workdays()
        duration = len(days)
        self.assertEqual(duration, 1, msg='duration 1 fail')

    def test_job_workdays_list(self):
        '''
        A 8 hours workday starting on a dayoff.
        '''
        jobworkday = JobSchedule(8, 8, datetime.date(2020, 11, 1))
        day1 = jobworkday.job_workdays()

        self.assertEqual(day1, [datetime.date(2020, 11, 2)], msg='day 1')

    def test_job_workdays_gt_1(self):
        '''
        workhours greater then hours of a workday
        '''
        jobworkday = JobSchedule(8, 4, datetime.date(2020, 11, 1))
        days = jobworkday.job_workdays()
        duration = len(days)
        self.assertEqual(duration, 2, msg='2 days')

    def test_job_workdays_partial_workday(self):
        '''
        workhours is minor then hours of a workday
        '''
        jobworkday = JobSchedule(3, 8, datetime.date(2020, 11, 1))
        days = jobworkday.job_workdays()
        duration = len(days)
        self.assertEqual(duration, 1, msg='partial day')

    def test_job_workdays_partial_workdays_list(self):
        '''
        workdays with 1.5hs per day
                November 2020
        Mo Tu We Th Fr Sa Su
                           1
         2  3  4  5  6  7  8
         9 10 11 12 13 14 15
        16 17 18 19 20 21 22
        23 24 25 26 27 28 29
        30
        '''
        jobworkday = JobSchedule(4.5, 1.5, datetime.date(2020, 11, 1))
        days = jobworkday.job_workdays()
        days_shouldbe = [
            datetime.date(2020, 11, 2),
            datetime.date(2020, 11, 3),
            datetime.date(2020, 11, 4)]
        self.assertEqual(
            days, days_shouldbe, msg='4.5hs job in 1.5hs workday'
        )

    def test_job_workdays_partial_workdays_duration(self):
        jobworkday = JobSchedule(8.5, 3.5, datetime.date(2020, 11, 1))
        days = jobworkday.job_workdays()
        duration = len(days)
        self.assertEqual(duration, 3, msg='3 days for 4.5hs job in 1.5hs workday')

    def test_job_workdays_predefined_networkdays(self):
        '''
        job scheduled workdays with predefined networkdays
        '''

        networkdays = Networkdays(
            datetime.date(2020, 11, 1),
            datetime.date(2020, 11, 30),
            [datetime.date(2020, 11, 29), ],  # holidays
            {1, 2, 3, 4, 5, 6})  # week days off

        jobworkday = JobSchedule(8.5, 3.5, datetime.date(2020, 11, 1), networkdays)
        days = jobworkday.job_workdays()

        days_shouldbe = [
            datetime.date(2020, 11, 1),
            datetime.date(2020, 11, 8),
            datetime.date(2020, 11, 15),
            ]

        self.assertEqual(days, days_shouldbe, msg='3 days for 8.5hs job in 3.5hs workday')

    def test_job_schedule_regards_jobs_startdate(self):
        '''
        Takes into account  the job start date, without ignore the networkdays calendar
        '''
        networkdays = Networkdays(
            datetime.date(2020, 11, 1),
            datetime.date(2020, 11, 30),
            )

        jobworkday = JobSchedule(8.5, 3.5, datetime.date(2020, 11, 7), networkdays)
        days = jobworkday.job_workdays()

        days_shouldbe = [
            datetime.date(2020, 11, 9),
            datetime.date(2020, 11, 10),
            datetime.date(2020, 11, 11),
            ]

        self.assertEqual(days, days_shouldbe, msg='3 days for 8.5hs job in 3.5hs workday')


    def test_job_schedule_get_years(self):
        '''
        Takes into account  the job start date, without ignore the networkdays calendar
        '''
        networkdays = Networkdays(
            datetime.date(2020, 12, 23),
            datetime.date(2021, 1, 4),
            )

        jobworkday = JobSchedule(80, 8, datetime.date(2020, 11, 7), networkdays)

        self.assertEqual(list(jobworkday.years()),[2020, 2021] )


    def test_job_schedule_get_months(self):
        '''
        Takes into account  the job start date, without ignore the networkdays calendar
        '''
        networkdays = Networkdays(
            datetime.date(2020, 12, 23),
            datetime.date(2021, 1, 4),
            )

        jobschedule = JobSchedule(80, 8, datetime.date(2020, 11, 7), networkdays)

        self.assertEqual(list(jobschedule.months()),[12, 1] )


    def test_job_schedule_get_months_filter(self):
        '''
        Takes into account  the job start date, without ignore the networkdays calendar
        '''
        networkdays = Networkdays(
            datetime.date(2020, 12, 23),
            datetime.date(2021, 1, 4),
            )

        jobschedule = JobSchedule(80, 8, datetime.date(2020, 11, 7), networkdays)

        self.assertEqual(list(jobschedule.months(year=2021)),[1,] )


    def test_job_schedule_get_weeks(self):
        '''
        Takes into account  the job start date, without ignore the networkdays calendar
        '''
        schdl_start = datetime.date(2021, 1, 3) # the year dint start on monday!
        schdl_finish = datetime.date(2021, 1, 31)

        networkdays = Networkdays(schdl_start, schdl_finish)

        jobschedule = JobSchedule(5000, 8, schdl_start, networkdays)

        self.assertEqual(list(jobschedule.weeks()),[1, 2, 3, 4] )


    def test_job_schedule_get_weeks_filter_year(self):
        '''

        '''
        schdl_start = datetime.date(2020, 12, 1)
        schdl_finish = datetime.date(2021, 1, 31)

        networkdays = Networkdays(schdl_start, schdl_finish)

        jobschedule = JobSchedule(5000, 8, schdl_start, networkdays)

        self.assertEqual(list(jobschedule.weeks(year=2021)),[53, 1, 2, 3, 4] )


    def test_job_schedule_get_weeks_filter_month(self):
        '''

        '''
        schdl_start = datetime.date(2020, 12, 1)
        schdl_finish = datetime.date(2021, 1, 31)

        networkdays = Networkdays(schdl_start, schdl_finish)

        jobschedule = JobSchedule(5000, 8, schdl_start, networkdays)

        self.assertEqual(list(jobschedule.weeks(month=1)),[53, 1, 2, 3, 4] )


    def test_job_schedule_get_weeks_filter_y_nd_m(self):
        '''

        '''
        schdl_start = datetime.date(2020, 10, 1)
        schdl_finish = datetime.date(2021, 1, 31)

        networkdays = Networkdays(schdl_start, schdl_finish)

        jobschedule = JobSchedule(5000, 8, schdl_start, networkdays)

        self.assertEqual(list(jobschedule.weeks(year=2020, month=11)),[ 45, 46, 47, 48, 49] )


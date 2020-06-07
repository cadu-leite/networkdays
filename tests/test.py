import unittest
import datetime

from networkdays.networkdays import networkdays, job_workdays


class TestNetworkDays(unittest.TestCase):

    def test_networkdays_calc_days_qtt(self):

        number_wds_per_month_2020=[
            (datetime.date(2020, 1, 1), datetime.date(2020, 1, 31), 23.00, {}),
            (datetime.date(2020, 2, 1), datetime.date(2020, 2, 28), 20.00, {}),
            (datetime.date(2020, 3, 1), datetime.date(2020, 3, 31), 22.00, {}),
            (datetime.date(2020, 4, 1), datetime.date(2020, 4, 30), 22.00, {}),
            (datetime.date(2020, 5, 1), datetime.date(2020, 5, 31), 21.00, {}),
            (datetime.date(2020, 6, 1), datetime.date(2020, 6, 30), 22.00, {}),
            (datetime.date(2020, 7, 1), datetime.date(2020, 7, 31), 23.00, {}),
            (datetime.date(2020, 8, 1), datetime.date(2020, 8, 30), 20.00, {}),
            (datetime.date(2020, 9, 1), datetime.date(2020, 9, 30), 22.00, {}),
            (datetime.date(2020, 10, 1), datetime.date(2020, 10, 31), 22.00, {}),
            (datetime.date(2020, 11, 1), datetime.date(2020, 11, 30), 21.00, {}),
            (datetime.date(2020, 12, 1), datetime.date(2020, 12, 31), 23.00, {}),
            (datetime.date(2020, 12, 1), datetime.date(2020, 12, 31), 22.00, {
                datetime.date(2020, 12, 25),  # a holiday
            }),
            (datetime.date(2020, 8, 1),datetime.date(2020, 8, 30), 19.00, {
                datetime.date(2020, 8, 7), datetime.date(2020, 8, 15),  # two holidays, but 1 on saturday
            }),

        ]

        for date in number_wds_per_month_2020:
            with self.subTest(date=date):
                workdays = len(networkdays(date[0], date[1], date[3]))
                # 2020 Jun, has 22 work days considering no holidays
                self.assertEqual(workdays, date[2], msg='fail %s' % (date[0]))

    def test_networkdays_calc_days_qtt_workdaysoff(self):
        '''
        days list with custom days off per week
        workdays only sundays + holiday on sunday

        November 2020
        Mo Tu We Th Fr Sa Su
                           1
         2  3  4  5  6  7  8
         9 10 11 12 13 14 15
        16 17 18 19 20 21 22
        23 24 25 26 27 28 29
        30
        '''
        workdays = (
            networkdays(
                datetime.date(2020, 11, 1),
                datetime.date(2020, 11, 30),
                [datetime.date(2020, 11, 29), ], {1, 2, 3, 4, 5, 6})
        )
        self.assertEqual(len(workdays), 4, msg='fail weekdaysoff 1')

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
        days = job_workdays(8, 8, datetime.date(2020, 11, 1))
        duration = len(days)
        self.assertEqual(duration, 1, msg='duration 1 fail')

    def test_job_workdays_list(self):
        '''
        A 8 hours workday starting on sunday, but sunday forbidden
        '''
        day1 = job_workdays(8, 8, datetime.date(2020, 11, 1))
        self.assertEqual(day1, {datetime.date(2020, 11, 2)}, msg='day 1')

    def test_job_workdays_gt_1(self):
        '''
        workhours greater then a workday
        '''
        days = job_workdays(8, 4, datetime.date(2020, 11, 1))
        duration = len(days)
        self.assertEqual(duration, 2, msg='2 days')

    def test_job_workdays_partial_workday(self):
        '''
        workhours is less  then a workday (partial workday)
        '''
        days = job_workdays(3, 8, datetime.date(2020, 11, 1))
        duration = len(days)
        self.assertEqual(duration, 1, msg='partial day')

    def test_job_workdays_partial_workdays_list(self):
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
        days = job_workdays(4.5, 1.5, datetime.date(2020, 11, 1))
        days_shouldbe = {
            datetime.date(2020, 11, 2),
            datetime.date(2020, 11, 3),
            datetime.date(2020, 11, 4)}
        self.assertEqual(
            days, days_shouldbe, msg='4.5hs job in 1.5hs workday'
        )

    def test_job_workdays_partial_workdays_duration(self):
        days = job_workdays(8.5, 3.5, datetime.date(2020, 11, 1))
        duration = len(days)
        self.assertEqual(duration, 3, msg='3 days for 4.5hs job in 1.5hs workday')

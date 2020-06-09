import unittest
import datetime

from networkdays.networkdays import Networkdays


class TestClassNetworkDays(unittest.TestCase):

    def test_networkdays_calc_days_number(self):
        '''
        number of workdays per month on 2020
        '''

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
                networkdays = Networkdays(date[0], date[1], date[3])
                # 2020 Jun, has 22 work days considering no holidays
                self.assertEqual(len(networkdays.networkdays()), date[2], msg='Class Test fail -> %s' % (date[0]))

    def test_networkdays_calc_days_number_workdaysoff(self):
        '''
        workdays with custom days off per week
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
        networkdays = Networkdays(
            datetime.date(2020, 11, 1),
            datetime.date(2020, 11, 30),
            [datetime.date(2020, 11, 29), ],  # holidays
            {1, 2, 3, 4, 5, 6})  # week days off
        workdays = networkdays.networkdays()
        self.assertEqual(len(workdays), 4, msg='fail weekdaysoff 1')

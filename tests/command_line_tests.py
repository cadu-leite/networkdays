from unittest import mock
from unittest import TestCase
import datetime

from networkdays import __main__ as ntwdmain

class TestDateFormats(TestCase):

    def test_call_with_nor_args(self):
        with self.assertRaises(SystemExit):
            ntwdmain.command_line_parser([])

    def test_call_with_year_only(self):
        args = ntwdmain.command_line_parser(['2020-12-12', ])
        self.assertEqual(args.date_initial, '2020-12-12')

    def test_call_with_year_initial_final(self):
        args = ntwdmain.command_line_parser(['-f', '2021', '2020-12-12'])
        self.assertEqual(args.date_final, '2021')
        self.assertEqual(args.date_initial, '2020-12-12')

    def test_complete_date_arg_initial_date(self):
        args = ntwdmain.command_line_parser(['2020-03-01'])
        self.assertEqual(ntwdmain.str_iso_date_to_date(args.date_initial), datetime.date(2020, 3, 1))

    def test_complete_date_arg_initial_date_no_padding_0(self):
        args = ntwdmain.command_line_parser(['2020-3-1'])
        self.assertEqual(ntwdmain.str_iso_date_to_date(args.date_initial), datetime.date(2020, 3, 1))

    def test_partial_year_arg_initial_date(self):
        args = ntwdmain.command_line_parser(['2020'])
        self.assertEqual(ntwdmain.str_iso_date_to_date(args.date_initial), datetime.date(2020, 1, 1))

    def test_partial_month_arg_initial_date(self):
        args = ntwdmain.command_line_parser(['2020-12'])
        self.assertEqual(ntwdmain.str_iso_date_to_date(args.date_initial), datetime.date(2020, 12, 1))

    def test_partial_wrong_month_arg_initial_date(self):
        with self.assertRaises(ValueError):
            args = ntwdmain.command_line_parser(['2020-13'])
            ntwdmain.str_iso_date_to_date(args.date_initial)

    def test_date_initial_date_final(self):
        args = ntwdmain.command_line_parser(['2020', '-f', '2021'])
        ntwdmain.str_iso_date_to_date(args.date_initial)
        self.assertEqual(ntwdmain.str_iso_date_to_date(args.date_final), datetime.date(2021, 1, 1))

    def test_networkdays_called_transformed_arguments(self):
        with mock.patch('networkdays.networkdays.Networkdays', auto_spec=True) as mocknetworkdays:
            ntwdmain.main(['-f', '2021', '2020'])
            mocknetworkdays.assert_called_with(datetime.date(2020, 1, 1), datetime.date(2021, 1, 1))

    def test_networkdays_called_month_transformed_arguments(self):
        with mock.patch('networkdays.networkdays.Networkdays', auto_spec=True) as mocknetworkdays:
            ntwdmain.main(['-f', '2020-05', '2020-04'])
            mocknetworkdays.assert_called_with(datetime.date(2020, 4, 1), datetime.date(2020, 5, 1))



import unittest
import subprocess
import sys

class TestCommandLineInterface(unittest.TestCase):
    """
    Tests for the command-line interface of the networkdays script.
    These tests execute the script as a subprocess to capture stdout, stderr,
    and the exit code, simulating real-world usage.
    """

    def run_cli(self, args):
        """
        Executes the CLI script as a subprocess.

        Args:
            args (list): A list of command-line arguments.

        Returns:
            tuple: A tuple containing (stdout, stderr, exit_code).
        """
        process = subprocess.run(
            [sys.executable, '-m', 'networkdays', *args],
            capture_output=True,
            text=True
        )
        return process.stdout, process.stderr, process.returncode

    def test_success_with_start_and_end_date(self):
        """
        Tests a successful run with a start and end date.
        Verifies the exact list of workdays is printed to stdout.
        """
        stdout, stderr, exit_code = self.run_cli(['2024-03-01', '-f', '2024-03-10'])

        self.assertEqual(exit_code, 0)
        self.assertEqual(stderr, '')

        # Expected output for workdays between Fri 2024-03-01 and Sun 2024-03-10
        # Workdays are: 1, 4, 5, 6, 7, 8
        expected_output = (
            "[datetime.date(2024, 3, 1), datetime.date(2024, 3, 4), "
            "datetime.date(2024, 3, 5), datetime.date(2024, 3, 6), "
            "datetime.date(2024, 3, 7), datetime.date(2024, 3, 8)]\n"
        )
        self.assertEqual(stdout, expected_output)

    def test_success_with_start_date_only(self):
        """
        Tests a successful run with only a start date.
        The end date should default to one year after the start date.
        """
        # The output is long, so we'll just check for success and that the output
        # starts and ends with the expected dates.
        stdout, stderr, exit_code = self.run_cli(['2024-12-25'])

        self.assertEqual(exit_code, 0)
        self.assertEqual(stderr, '')

        # Starts on Christmas 2024 (Wednesday)
        self.assertTrue(stdout.strip().startswith('[datetime.date(2024, 12, 25),'))
        # The range is inclusive, so 2025-12-25 is the last day checked.
        # It's a Thursday and not a default holiday.
        self.assertTrue(stdout.strip().endswith('datetime.date(2025, 12, 25)]'))

    def test_success_with_partial_date(self):
        """
        Tests a successful run using partial dates (YYYY-MM).
        """
        stdout, stderr, exit_code = self.run_cli(['2024-02', '-f', '2024-03'])

        self.assertEqual(exit_code, 0)
        self.assertEqual(stderr, '')

        # Should be equivalent to 2024-02-01 to 2024-03-01
        # Workdays in Feb 2024 (leap year): 21 days
        # Workdays in Mar 2024 (up to 1st): 1 day (Fri)
        # Total: 22 workdays
        self.assertTrue(stdout.strip().startswith('[datetime.date(2024, 2, 1),'))
        self.assertTrue(stdout.strip().endswith('datetime.date(2024, 3, 1)]'))
        self.assertEqual(stdout.count('datetime.date'), 22)

    def test_error_no_arguments(self):
        """
        Tests that the script exits with an error when no arguments are given.
        """
        stdout, stderr, exit_code = self.run_cli([])

        self.assertNotEqual(exit_code, 0)
        self.assertEqual(stdout, '')
        self.assertIn('usage: __main__.py [-h]', stderr)
        self.assertIn('the following arguments are required: date_initial', stderr)

    def test_error_invalid_date_format(self):
        """
        Tests that the script exits with a clean error for an invalid date format.
        """
        stdout, stderr, exit_code = self.run_cli(['2024/01/01'])

        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout, '')
        self.assertEqual(stderr, 'Error: cant convert date "2024/01/01"\n')

    def test_error_invalid_date_value(self):
        """
        Tests that the script exits with a clean error for an invalid date value.
        """
        stdout, stderr, exit_code = self.run_cli(['2024-02-30'])

        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout, '')
        self.assertEqual(stderr, 'Error: cant convert date "2024-02-30"\n')

    def test_help_argument(self):
        """
        Tests that the --help argument prints a help message and exits cleanly.
        """
        for arg in ['-h', '--help']:
            with self.subTest(arg=arg):
                stdout, stderr, exit_code = self.run_cli([arg])
                self.assertEqual(exit_code, 0)
                self.assertEqual(stderr, '')
                self.assertIn('usage: __main__.py [-h]', stdout)
                self.assertIn('Bussiness Days Calendar & JobScheduling', stdout)
                self.assertIn('positional arguments:', stdout)
                self.assertIn('options:', stdout)

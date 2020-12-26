import argparse
import datetime
import sys
import re

from networkdays import networkdays


DESCRIPTION = 'Bussiness Days Calendar & JobScheduling'


def str_iso_date_to_date(partial_iso_date):
    '''
    Convert a string representing a ISO format Date into Python Datetime date.
    '''

    regcomp = re.compile(r'(?P<year>[0-9]{4})-*(?P<month>[0-1]*[0-9])*-*(?P<day>[0-3]*[0-9])*')
    d = regcomp.match(partial_iso_date)

    # cast to integer while replace `None` to `1`
    date_params = [int(d) if d is not None else 1 for d in d.groups()]

    try:
        date = datetime.date(*date_params)
    except ValueError:
        raise ValueError(f'Error: cant convert date "{partial_iso_date}"')
        date = None
    return date


def command_line_parser(sys_args):

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        'date_initial',
        help='initial date in iso format ...  yyyy-mm-dd. You may pass partial dates "yyyy-mm" or even "yyyy"'
    )
    parser.add_argument(
        '-f', '--date_final',
        help='final date in iso format ...  yyyy-mm-dd. You may pass partial dates "yyyy-mm" or even "yyyy"'
    )

    args = parser.parse_args(sys_args)
    return args


def main(sys_args):

    args = command_line_parser(sys_args)
    date_initial = str_iso_date_to_date(args.date_initial)
    if args.date_final:
        date_final = str_iso_date_to_date(args.date_final)
    else:
        date_final = None
    ndays = networkdays.Networkdays(date_initial, date_final)
    print(ndays.networkdays())
    # sys.stdout.write(f'{list(ndays.networkdays())}\n')  # \n need to sys not put promt just after output.

    # printout()


if __name__ == '__main__':
    main(sys.argv[1:])

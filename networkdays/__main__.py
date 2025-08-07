import argparse
import datetime
import sys
import re
from typing import List, Optional

from networkdays.networkdays import Networkdays


DESCRIPTION = 'Bussiness Days Calendar & JobScheduling'


def str_iso_date_to_date(partial_iso_date: str) -> datetime.date:
    '''
    Convert a string representing a ISO format Date into Python Datetime date.
    '''

    # New, stricter regex anchors to the start/end of the string.
    regcomp = re.compile(r'^(\d{4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?$')
    d = regcomp.match(partial_iso_date)

    if d is None:
        raise ValueError(f'Error: cant convert date "{partial_iso_date}"')

    # The groups are now ('YYYY', 'MM' or None, 'DD' or None)
    # cast to integer while replace `None` to `1`
    date_params_str = d.groups()
    date_params = [int(p) if p is not None else 1 for p in date_params_str]

    try:
        date = datetime.date(*date_params)
    except ValueError:
        # This will catch things like month > 12 or day > 31
        raise ValueError(f'Error: cant convert date "{partial_iso_date}"')
    return date


def command_line_parser(sys_args: List[str]) -> argparse.Namespace:

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


def main(sys_args: List[str]) -> None:
    try:
        args = command_line_parser(sys_args)
        date_initial = str_iso_date_to_date(args.date_initial)
        date_final: Optional[datetime.date] = None
        if args.date_final:
            date_final = str_iso_date_to_date(args.date_final)

        ndays = Networkdays(date_initial, date_final)
        print(ndays.networkdays())

    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])

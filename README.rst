***********
Networkdays
***********

-------------------------------------------

.. image:: https://img.shields.io/pypi/v/python-networkdays.svg?style=flat-square
    :target: https://pypi.org/project/python-networkdays
    :alt: pypi version


.. image:: https://readthedocs.org/projects/networkdays/badge/?version=latest
    :target: https://networkdays.readthedocs.io/?badge=latest
    :alt: Documentation Status


.. image:: https://codecov.io/gh/cadu-leite/networkdays/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/cadu-leite/networkdays
    :alt: code coverage

-------------------------------------------


- Business days calendar.
- JobSchedule on business days.

.. tip::

    **Just Python built-in libs, no dependencies**


Networkdays:
    Return working days between two dates exclude weekends and holidays.

    - just like spreadsheets `networdays` function
    - exclude Holidays
    - Exclude "days off" per week.


Job schedule:
    Calculate the period for a given job hours, based on `Networdays`.


.. contents:: Table of Contents


Installation
============

python-networkdays can be installed from PyPI using pip

.. code-block:: bash

    pip install python-networkdays

.. tip:: note that the package name is different from the importable name

Page on Pypi: https://pypi.org/project/python-networkdays/

There is no dependencies.


Features
========

- Return a list of business days between 2 dates.
- Exclude weekends by default
- Custom "days off" may be informed as list like {1,2,3,4,5,6,7}, where 1 is Monday default is {6,7} = (Sat, Sun).
- How many business days between two dates.
- How many days off, including holidays and weekends.
- Return a list of business days for a given number of hours
- Return a list of Years, months or weeks for a given number of hours
- **No Pandas or NumPy dependencies**


Examples
========

Networkdays.networkdays()
-------------------------

.. code:: python

    >>> import datetime
    >>> from networkdays import networkdays

    >>> HOLIDAYS = { datetime.date(2020, 12, 25) }

    >>> days = networkdays.Networkdays(datetime.date(2020, 12, 1), datetime.date(2020, 12, 25), HOLIDAYS) #todo: this was not defined before this, Cadu needs to define it
    >>> # you have methods to get holidays and weekends date list as well.
    >>> # here i just got the size of each set
    >>> f'Bussiness days: {len(days.networkdays())} {days.networkdays()[:2]}...{days.networkdays()[-2:]}'
    'Bussiness days: 18 [datetime.date(2020, 12, 1), datetime.date(2020, 12, 2)]...[datetime.date(2020, 12, 23), datetime.date(2020, 12, 24)]'
    >>> f'Weekends: {len(days.weekends())} {days.weekends()[:2]} ...{days.weekends()[-2:]}'
    'Weekends: 6 [datetime.date(2020, 12, 5), datetime.date(2020, 12, 6)] ...[datetime.date(2020, 12, 19), datetime.date(2020, 12, 20)]'
    >>> f'Holidays: {len(days.holidays())}'
    'Holidays: 1'


Networkdays.jobschedule()
-------------------------

.. code:: python

    >>> # Distribute the 600 hrs of effort, starting on december 1, 2020 working 8hrs per day.
    >>> jobschedule = networkdays.JobSchedule(600, 8, datetime.date(2020, 12, 1), networkdays=None)
    >>> job_dates = jobschedule.job_workdays()
    >>> jobschedule.bussines_days
    54
    >>> jobschedule.total_days
    datetime.timedelta(days=73)
    >>> jobschedule.prj_starts
    '12/01/20'
    >>> jobschedule.prj_ends
    '02/12/21'
    >>> list(jobschedule.years())
    [2020, 2021]
    >>> list(jobschedule.months())
    [12, 1, 2]
    >>> list(jobschedule.weeks()) # ISO
    [49, 50, 51, 52, 53, 1, 2, 3, 4, 5, 6]
    >>> f'days: {list(jobschedule.days())[:2]} ... {list(jobschedule.days())[-2:]}'
    'days: [datetime.date(2020, 12, 1), datetime.date(2020, 12, 2)] ... [datetime.date(2021, 2, 11), datetime.date(2021, 2, 12)]'

Other similar projects
======================

When I start to code, I did check for some similar projects.

I knew about `python-dateutil <https://github.com/dateutil/dateutil>`_, a great project I use for years...
I'd like something more straightforward or simpler.

After to publish the python-networkdays on PyPi
I found some others  8(

- workdays_ : A 5 years old project, looks the same as networkdays_
- timeboard_ : A more complex but powerful project
- python-dateutil_ is great, powerful but even more complex.
- python-bizdays_ : Quick simple and direct ...

.. _workdays: https://pypi.org/project/workdays/
.. _timeboard: https://github.com/mmamaev/timeboard
.. _python-dateutil: https://github.com/dateutil/dateutil
.. _python-bizdays: https://github.com/wilsonfreitas/python-bizdays

I will try to keep this list updated...


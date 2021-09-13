***********
Networkdays
***********

some statistics ...

+------------------------+----------------------+--------------------+---------------------+
| Pypi Version           | Doc Status           | Coverage           | Downloads           |
+========================+======================+====================+=====================+
|  |badge_pypi_version|  |  |badge_doc_status|  |  |badge_coverage|  |  |badge_downloads|  |
+------------------------+----------------------+--------------------+---------------------+


.. |badge_pypi_version| image:: https://img.shields.io/pypi/v/python-networkdays.svg?style=flat-square
    :target: https://pypi.org/project/python-networkdays
    :alt: pypi version


.. |badge_doc_status| image:: https://readthedocs.org/projects/networkdays/badge/?version=latest
    :target: https://networkdays.readthedocs.io/?badge=latest
    :alt: Documentation Status


.. |badge_coverage| image:: https://codecov.io/gh/cadu-leite/networkdays/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/cadu-leite/networkdays
    :alt: code coverage


.. |badge_downloads| image:: https://img.shields.io/pypi/dm/wagtail-seo
    :target: https://pypi.org/project/python-networkdays
    :alt: Downloads on Pypi


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

Class Networkdays.networkdays
-----------------------------

List business days, weekends and Holidays
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. code-block:: python
    
    In [1]: from networkdays import networkdays

    In [2]: import datetime

    In [3]: HOLIDAYS = { datetime.date(2020, 12, 25) }  # define a Holidays list

    # initiate  class::`networkdays.Networkdays` 
    In [4]: days = networkdays.Networkdays(
                datetime.date(2020, 12, 15),  # start date
                datetime.date(2020, 12, 31),  # end date
                HOLIDAYS  # list of Holidays
            )

    In [5]: days.networkdays()  # return a list os workdays 
    Out[5]:
    [datetime.date(2020, 12, 15),
     datetime.date(2020, 12, 16),
     datetime.date(2020, 12, 17),
     datetime.date(2020, 12, 18),
     datetime.date(2020, 12, 21),
     datetime.date(2020, 12, 22),
     datetime.date(2020, 12, 23),
     datetime.date(2020, 12, 24),
     datetime.date(2020, 12, 28),
     datetime.date(2020, 12, 29),
     datetime.date(2020, 12, 30),
     datetime.date(2020, 12, 31)]

    In [6]: days.weekends()  # list os Weekends (default = Saturday ans Sunday) 
    Out[6]:
    [datetime.date(2020, 12, 19),
     datetime.date(2020, 12, 20),
     datetime.date(2020, 12, 26),
     datetime.date(2020, 12, 27)]

    In [7]: days.holidays()
    Out[7]: [datetime.date(2020, 12, 25)] # list of holidays 


class Networkdays.jobschedule
-----------------------------

.. code-block:: python

    >>> from networkdays import networkdays
    >>> import datetime
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


More on ..  

https://networkdays.readthedocs.io/index.html

https://libraries.io/pypi/python-networkdays/sourcerank

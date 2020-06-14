***********
Networkdays
***********


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



Examples
========

Networkdays.networkdays()
-------------------------

.. code:: python

    # Networkdays, given  December 2020, calendar...
    #
    #  December 2020
    #  Mo Tu We Th Fr Sa Su
    #      1  2  3  4  5  6
    #   7  8  9 10 11 12 13
    #  14 15 16 17 18 19 20
    #  21 22 23 24 25 26 27
    #  28 29 30 31


    import datetime
    from networkdays import networkdays

    HOLIDAYS  = [
        datetime.date(2020, 12, 25), # World Peace Day
        datetime.date(2020, 9, 7),   # a **fake** holiday out of period
    ]

    # networkdays between 2020-12-01 and 2020-12-31 and week days off *default*(Sut and Sun)
    days = networkdays.Networkdays(datetime.date(2020, 12, 1), datetime.date(2020, 12, 31), holidays=HOLIDAYS)
    print(days.networkdays())


results ...

.. parsed-literal::

    [datetime.date(2020, 12, 1), datetime.date(2020, 12, 2),
    datetime.date(2020, 12, 3), datetime.date(2020, 12, 4),
    ...
    datetime.date(2020, 12, 28), datetime.date(2020, 12, 29),
    datetime.date(2020, 12, 30), datetime.date(2020, 12, 31)]


.. code:: python

    # you have methods to get holidays and weekends date list as well.
    # here i just got the size of each set
    print(f'''
    Qtt bussines days: {len(days.networkdays())}
    Qtt Weekends: {len(days.weekends())}
    Qtt Holidays: {len(days.holidays())}
    ''')
    print(days.weekends())


.. parsed-literal::

    Dates work: 22
    Dates Weekends: 8
    Dates Holidays: 1

    [datetime.date(2020, 12, 5), datetime.date(2020, 12, 6),
    datetime.date(2020, 12, 12), datetime.date(2020, 12, 13),
    datetime.date(2020, 12, 19), datetime.date(2020, 12, 20),
    datetime.date(2020, 12, 26), datetime.date(2020, 12, 27)]


Networkdays.jobschedule()
-------------------------

.. code:: python

    # jobSchedule
    import datetime

    from networkdays import networkdays
    DATE_START = datetime.date(2020, 12, 1)

    # Distribute the 600 hrs of effort, starting on december 1, 2020 workin 8hrs per day.
    jobschedule = networkdays.JobSchedule(600, 8, DATE_START, networkdays=None)
    job_dates = jobschedule.job_workdays()

.. code:: python

    print(f'''
    project_duration_hours: {jobschedule.project_duration_hours}'
    date_start:             {jobschedule.date_start}
    workhours_per_day:      {jobschedule.workhours_per_day}

    bussines days:          {jobschedule.bussines_days}
    calendar days:          {jobschedule.total_days}
    starts:                 {jobschedule.prj_starts}
    ends:                   {jobschedule.prj_ends}

    years:                  {list(jobschedule.years())}
    months:                 {list(jobschedule.months())}
    weeks (ISO):            {list(jobschedule.weeks())}
    days:                   {list(jobschedule.days())[:2]} ...\n\t\t\t ...{list(jobschedule.days())[-2:]}
    Works days dates on january: {list(jobschedule.days())[:2]} ...\n\t\t\t ...{list(jobschedule.days())[-2:]}
    ''')


.. parsed-literal::


    project_duration_hours: 600'
    date_start:             2020-12-01
    workhours_per_day:      8

    bussines days:          54
    calendar days:          73 days, 0:00:00
    starts:                 12/01/20
    ends:                   02/12/21

    years:                  [2020, 2021]
    months:                 [12, 1, 2]
    weeks (ISO):            [49, 50, 51, 52, 53, 1, 2, 3, 4, 5, 6]
    days:                   [datetime.date(2020, 12, 1), datetime.date(2020, 12, 2)] ...
                 ...[datetime.date(2021, 2, 11), datetime.date(2021, 2, 12)]
    Works days dates on january: [datetime.date(2020, 12, 1), datetime.date(2020, 12, 2)] ...
                 ...[datetime.date(2021, 2, 11), datetime.date(2021, 2, 12)]



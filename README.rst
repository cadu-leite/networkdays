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

    import datetime
    from networkdays import networkdays

    HOLIDAYS  = { datetime.date(2020, 12, 25),}

    days = networkdays.Networkdays(datetime.date(2020, 12, 1), datetime.date(2020, 12, 31), holidays=HOLIDAYS)

    # you have methods to get holidays and weekends date list as well.
    # here i just got the size of each set
    print(f'''
    Bussiness days: {len(days.networkdays())}
        {days.networkdays()[:2]}
        ...{days.networkdays()[-2:]}

    Weekends:       {len(days.weekends())}
        {days.weekends()[:2]}
        ...{days.weekends()[-2:]}

    Holidays:       {len(days.holidays())}
    ''')


.. parsed-literal::


    Bussiness days: 22
        [datetime.date(2020, 12, 1), datetime.date(2020, 12, 2)]
        ...[datetime.date(2020, 12, 30), datetime.date(2020, 12, 31)]

    Weekends:       8
        [datetime.date(2020, 12, 5), datetime.date(2020, 12, 6)]
        ...[datetime.date(2020, 12, 26), datetime.date(2020, 12, 27)]

    Holidays:       1



Networkdays.jobschedule()
-------------------------

.. code:: python

    # jobSchedule
    import datetime
    from networkdays import networkdays

    # Distribute the 600 hrs of effort, starting on december 1, 2020 working 8hrs per day.
    jobschedule = networkdays.JobSchedule(600, 8, datetime.date(2020, 12, 1), networkdays=None)
    job_dates = jobschedule.job_workdays()

    # print results ...
    print(f'''

    bussines days:          {jobschedule.bussines_days}
    calendar days:          {jobschedule.total_days}
    starts - ends:          {jobschedule.prj_starts} - {jobschedule.prj_ends}

    years:                  {list(jobschedule.years())}
    months:                 {list(jobschedule.months())}
    weeks (ISO):            {list(jobschedule.weeks())}

    days:
        {list(jobschedule.days())[:2]} ...\n ...{list(jobschedule.days())[-2:]}

    Works days dates on january:
        {list(jobschedule.days())[:2]} ...\n ...{list(jobschedule.days())[-2:]}
    ''')


.. parsed-literal::



    bussines days:          54
    calendar days:          73 days, 0:00:00
    starts - ends:          12/01/20 - 02/12/21

    years:                  [2020, 2021]
    months:                 [12, 1, 2]
    weeks (ISO):            [49, 50, 51, 52, 53, 1, 2, 3, 4, 5, 6]

    days:
        [datetime.date(2020, 12, 1), datetime.date(2020, 12, 2)] ...
     ...[datetime.date(2021, 2, 11), datetime.date(2021, 2, 12)]

    Works days dates on january:
        [datetime.date(2020, 12, 1), datetime.date(2020, 12, 2)] ...
     ...[datetime.date(2021, 2, 11), datetime.date(2021, 2, 12)]


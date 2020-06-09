
***********
Networkdays
***********


Networkdays functions ...  including `networkdays` excel like function



Example
=======


Given September 2020::

       September 2020
    Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6
     7  8  9 10 11 12 13  Monday, 7 - Brazil Independence day.
    14 15 16 17 18 19 20
    21 22 23 24 25 26 27
    28 29 30


Workdays between 1 to 10 September 2020
---------------------------------------

.. code-block:: python

    import datetime
    from networkdays import networkdays
    nwds = networkdays.Networkdays(
        datetime.date(2020, 9, 1), datetime.date(2020, 9, 10),
        holidays=[datetime.date(2020, 9, 7)]  # Brazil independence day
    )
    workdays = nwds.networkdays()

    print(f'dates: {workdays}')

    print(f'Number of Workdays for November: {len(workdays)}')

Returns workdays between September 1 - 10 ::

    dates: [
        datetime.date(2020, 9, 1),datetime.date(2020, 9, 2),datetime.date(2020, 9, 3),datetime.date(2020, 9, 4),
        datetime.date(2020, 9, 8),datetime.date(2020, 9, 9),datetime.date(2020, 9, 10)
    ]

    Number of Workdays for November 1-10: 7


55hs Job Schedule starting 1 September 2020 - workday 8hs /day
--------------------------------------------------------------


.. code-block:: python

    import datetime
    from networkdays import networkdays

    # 55hs job for 8hs/day, starting 1 September 2020.
    schdl = networkdays.JobSchedule(55, 8, datetime.date(2020, 7, 1))
    schdl.job_workdays()

returns ::

    [datetime.date(2020, 7, 1),
     datetime.date(2020, 7, 2),
     datetime.date(2020, 7, 3),
     datetime.date(2020, 7, 6),
     datetime.date(2020, 7, 7),
     datetime.date(2020, 7, 8)]


...   7 September is National Holiday
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. code-block:: python


    nwds = networkdays.Networkdays(
        datetime.date(2020, 9, 1), datetime.date(2020, 9, 10), # date start -> end
        holidays=[datetime.date(2020, 9, 7)],  # datetime.date holidays list
        weekdaysoff = {6,7} # iso weekdays indicating week days off.
    )
    workdays = nwds.networkdays()

    schdl = networkdays.JobSchedule(55, 8, datetime.date(2020, 9, 1), nwds)
    schdl.job_workdays()

results ::

    [
        datetime.date(2020, 9, 1),
        datetime.date(2020, 9, 2),
        datetime.date(2020, 9, 3),
        datetime.date(2020, 9, 4),
        datetime.date(2020, 9, 8),
        datetime.date(2020, 9, 9),
        datetime.date(2020, 9, 10)
    ]



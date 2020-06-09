
***********
Networkdays
***********



Networkdays functions ...  including `networkdays` excel like function



Example
=======


given September 2020::

       September 2020
    Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6
     7  8  9 10 11 12 13  Monday, 7 - Brazyl Independence day.
    14 15 16 17 18 19 20
    21 22 23 24 25 26 27
    28 29 30


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

returns ::

    dates: [
        datetime.date(2020, 9, 1),datetime.date(2020, 9, 2),datetime.date(2020, 9, 3),datetime.date(2020, 9, 4),
        datetime.date(2020, 9, 8),datetime.date(2020, 9, 9),datetime.date(2020, 9, 10)
    ]

    Number of Workdays for November 1-10: 7


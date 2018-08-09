#!/usr/bin/python
from __future__ import print_function
from datetime import timedelta
from datetime import datetime
from pprint import pprint


def main():
    st = datetime(2018, 8, 3, 13, 00, 00)
    et = datetime(2018, 8, 5, 14, 00, 00)
    GetDelta(st, et)

    st = datetime(2018, 8, 3, 00, 00, 00)
    et = datetime(2018, 8, 5, 14, 00, 00)
    GetDelta(st, et)

    st = datetime(2018, 8, 3, 00, 00, 00)
    et = datetime(2018, 8, 5, 00, 00, 00)
    GetDelta(st, et)

    st = datetime(2018, 8, 3, 00, 00, 00)
    et = datetime(2018, 8, 4, 00, 00, 00)
    GetDelta(st, et)

    st = datetime(2018, 8, 3, 00, 00, 00)
    et = datetime(2018, 8, 3, 00, 00, 00)
    GetDelta(st, et)

    st = datetime(2018, 8, 3, 00, 00, 00)
    et = datetime(2018, 8, 3, 1, 00, 00)
    GetDelta(st, et)

    st = datetime(2018, 8, 3, 1, 00, 00)
    et = datetime(2018, 8, 3, 2, 00, 00)
    GetDelta(st, et)


def GetDelta(st, et):
    dct = {}
    tDelta = timedelta(hours=24)

    nextDay = st.date().__add__(tDelta)
    nextDate = datetime.combine(nextDay, datetime.min.time())

    endDate = datetime.combine(et.date().__add__(tDelta), datetime.min.time())

    # if nextDate > et:
    #    dct[st.date()] = (et - st).total_seconds() / 60
    # else:
    while nextDate <= endDate:
        t = (min(nextDate, et) - st).total_seconds() / 60
        if t != 0:
            dct[st.date()] = t

        st = nextDate
        nextDay = nextDay.__add__(tDelta)
        nextDate = datetime.combine(nextDay, datetime.min.time())

    # p1 = et.date() - st.date()

    print("Starting")
    print("ST = ", st)
    print("ET = ", et)

    pprint(dct)


if __name__ == "__main__":
    main()

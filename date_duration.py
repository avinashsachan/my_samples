#!/usr/bin/python
#from __future__ import print_function
from datetime import timedelta
from datetime import datetime


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
    #print("Starting")
    #print("ST = ", st)
    #print("ET = ", et)

    return dct



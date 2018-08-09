#!/usr/bin/python
from __future__ import print_function
from datetime import timedelta
from datetime import datetime
from pprint import pprint
import date_duration as util


def main():
    st = datetime(2018, 8, 3, 13, 00, 00)
    et = datetime(2018, 8, 5, 14, 00, 00)
    print(util.GetDelta(st, et))

    st = datetime(2018, 8, 3, 00, 00, 00)
    et = datetime(2018, 8, 5, 14, 00, 00)
    print(util.GetDelta(st, et))

    st = datetime(2018, 8, 3, 00, 00, 00)
    et = datetime(2018, 8, 5, 00, 00, 00)
    print(util.GetDelta(st, et))

    st = datetime(2018, 8, 3, 00, 00, 00)
    et = datetime(2018, 8, 4, 00, 00, 00)
    print(util.GetDelta(st, et))

    st = datetime(2018, 8, 3, 00, 00, 00)
    et = datetime(2018, 8, 3, 00, 00, 00)
    print(util.GetDelta(st, et))

    st = datetime(2018, 8, 3, 00, 00, 00)
    et = datetime(2018, 8, 3, 1, 00, 00)
    print(util.GetDelta(st, et))

    st = datetime(2018, 8, 3, 1, 00, 00)
    et = datetime(2018, 8, 3, 2, 00, 00)
    print(util.GetDelta(st, et))


if __name__ == "__main__":
    main()

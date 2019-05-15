from unittest import TestCase
from datetime import datetime, date
from date_duration import date_duration as util
import unittest

class TestDate_duration(TestCase):
    def test_GetDeltaSameDay(self):
        st = datetime(2018, 8, 3, 1, 00, 00)
        et = datetime(2018, 8, 3, 2, 00, 00)
        r = util.GetDelta(st, et)
        r2 = {date(2018, 8, 3): 60}
        self.assertDictEqual(r, r2, "Failed")

    def test_GetDeltaSameDayRangeStartsAt00(self):
        st = datetime(2018, 8, 3, 00, 00, 00)
        et = datetime(2018, 8, 3, 14, 00, 00)
        r = util.GetDelta(st, et)
        r2 = {date(2018, 8, 3): 840.0}
        self.assertDictEqual(r, r2, "Failed")

    def test_GetDeltaMultiDayRange(self):
        st = datetime(2018, 8, 3, 13, 00, 00)
        et = datetime(2018, 8, 5, 14, 00, 00)
        r = util.GetDelta(st, et)
        r2 = {date(2018, 8, 3): 660,
              date(2018, 8, 4): 1440.0,
              date(2018, 8, 5): 840.0
              }
        self.assertDictEqual(r, r2, "Failed")

    def test_GetDeltaMultiDayRangeStartsAt00(self):
        st = datetime(2018, 8, 3, 00, 00, 00)
        et = datetime(2018, 8, 5, 14, 00, 00)
        r = util.GetDelta(st, et)
        r2 = {date(2018, 8, 3): 1440.0,
              date(2018, 8, 4): 1440.0,
              date(2018, 8, 5): 840.0
              }
        self.assertDictEqual(r, r2, "Failed")

    def test_GetDeltaMultiDayRangeStartsAt00EndsAt00(self):
        st = datetime(2018, 8, 3, 00, 00, 00)
        et = datetime(2018, 8, 5, 00, 00, 00)
        r = util.GetDelta(st, et)
        r2 = {date(2018, 8, 3): 1440.0,
              date(2018, 8, 4): 1440.0
              }
        self.assertDictEqual(r, r2, "Failed")
        

    def test_GetDeltaOneDayRangeStartsAt00EndsAt00(self):
        st = datetime(2018, 8, 3, 00, 00, 00)
        et = datetime(2018, 8, 4, 00, 00, 00)
        r = util.GetDelta(st, et)
        r2 = {date(2018, 8, 3): 1440.0
              }
        self.assertDictEqual(r, r2, "Failed")

    def test_GetDeltaZeroStartsAt00EndsAt00(self):
        st = datetime(2018, 8, 3, 00, 00, 00)
        et = datetime(2018, 8, 3, 00, 00, 00)
        r = util.GetDelta(st, et)
        r2 = {}
        self.assertDictEqual(r, r2, "Failed")

if __name__=="__main__":
    unittest.main()

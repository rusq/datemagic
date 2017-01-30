#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import unittest
import datetime
sys.path.append("..")
import datemagic as df


class TestDateInterval(unittest.TestCase):

    def test_split_interval_wrapper(self):
        self.assertEqual(df.split_interval(datetime.date(2016, 12, 1),
                                           datetime.date(2017, 1, 31)),
                         df.split_interval_int(12, 1, 2016, 1, 31, 2017))

    def test_split_interval_int(self):
        sample = [(datetime.date(2016, 12, 1), datetime.date(2016, 12, 30)),
                  (datetime.date(2016, 12, 31), datetime.date(2017, 1, 29)),
                  (datetime.date(2017, 1, 30), datetime.date(2017, 1, 31))]
        result = df.split_interval_int(12, 1, 2016, 1, 31, 2017)
        self.assertEqual(sample, result)

    def test_split_interval(self):
        sample = [(datetime.date(2016, 12, 1), datetime.date(2016, 12, 30)),
                  (datetime.date(2016, 12, 31), datetime.date(2017, 1, 29)),
                  (datetime.date(2017, 1, 30), datetime.date(2017, 1, 31))]
        result = df.split_interval(datetime.date(2016, 12, 1),
                                   datetime.date(2017, 1, 31))
        self.assertEqual(sample, result)

    def test_split_interval_one_day(self):
        sample = [(datetime.date(2016, 12, 1), datetime.date(2016, 12, 1))]
        result = df.split_interval(datetime.date(2016, 12, 1),
                                   datetime.date(2016, 12, 1))
        self.assertEqual(sample, result)

    def test_split_interval_inverse(self):
        sample = [(datetime.date(2016, 12, 1), datetime.date(2016, 12, 30)),
                  (datetime.date(2016, 12, 31), datetime.date(2017, 1, 29)),
                  (datetime.date(2017, 1, 30), datetime.date(2017, 1, 31))]
        result = df.split_interval(datetime.date(2017, 1, 31),
                                   datetime.date(2016, 12, 1))
        self.assertEqual(sample, result)

    def test_split_interval_no_enddate(self):
        sample = df.split_interval(datetime.date(2016, 12, 1),
                                   datetime.datetime.now().date())
        result = df.split_interval(datetime.date(2016, 12, 1))
        self.assertEqual(sample, result)

    def test_split_interval_int_no_enddate(self):
        sample = df.split_interval(datetime.date(2016, 12, 1),
                                   datetime.datetime.now().date())
        result = df.split_interval_int(12, 1, 2016)
        self.assertEqual(sample, result)

    def test_split_interval_day_chunk(self):
        sample = df.split_interval(datetime.date(2016, 12, 1),
                                   datetime.date(2016, 12, 31), chunksize=1)
        self.assertEqual(len(sample), 31)
        sample = df.split_interval(datetime.date(2016, 12, 1),
                                   datetime.date(2016, 12, 31), chunksize=2)
        self.assertEqual(len(sample), 16)

if __name__ == '__main__':
    unittest.main()

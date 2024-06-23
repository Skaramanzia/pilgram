import unittest
from datetime import timedelta

import numpy as np

from pilgram.utils import PathDict, read_update_interval
from pilgram.flags import LuckFlag, MoneyFlag, XpFlag


class TestUtils(unittest.TestCase):

    def test_pathdict(self):
        pd = PathDict({'a': 1, 'b': 2, 'c': 3, "d": {"e": 4}})
        self.assertEqual(pd.path_get("a"), 1)
        self.assertEqual(pd.path_get("b"), 2)
        self.assertEqual(pd.path_get("c"), 3)
        self.assertEqual(pd.path_get("d.e"), 4)
        pd = PathDict()
        pd.path_set("a.b.c", 1)
        self.assertEqual(pd.path_get("a.b.c"), 1)

    def test_interval_reading(self):
        interval_string = "6h"
        interval = read_update_interval(interval_string)
        self.assertEqual(interval, timedelta(hours=6))
        interval_string = "4h 30m 25s"
        interval = read_update_interval(interval_string)
        self.assertEqual(interval, timedelta(hours=4, minutes=30, seconds=25))
        interval_string = "4w 3d 2s"
        interval = read_update_interval(interval_string)
        self.assertEqual(interval, timedelta(weeks=4, days=3, seconds=2))

    def test_flags(self):
        flags = np.uint32(0)
        flags = LuckFlag.set(flags)
        flags = XpFlag.set(flags)
        flags = MoneyFlag.set(flags)
        self.assertEqual(np.binary_repr(flags), "111")

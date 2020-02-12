"""
This is the test suite for trade.py.
"""

from unittest import TestCase, main

from capital.trade_utils import endow, get_rand_good, is_depleted, AMT_AVAILABLE, transfer


class TradeUtilsTestCase(TestCase):
    def setUp(self, props=None):
        pass

    def tearDown(self):
        pass

    def test_endow(self):
        """
        See capital.trade_utils for description of what a
        `trader` and `goods` must look like.
        """
        goodA = {AMT_AVAILABLE: 10}
        goodB = {AMT_AVAILABLE: 10}
        trader = {"goods": {}}
        goods = {"a": goodA, "b": goodB}
        endow(trader, goods)
        self.assertFalse(is_depleted(trader["goods"]))

    def test_is_depleted(self):
        goods_dict_empty = {}
        goodA = {AMT_AVAILABLE: 0}
        goodB = {AMT_AVAILABLE: 0}
        goods_dict_zeros = {"a": goodA, "b": goodB}
        self.assertTrue(is_depleted(goods_dict_empty))
        self.assertTrue(is_depleted(goods_dict_zeros))

    def test_get_rand_good(self):
        goodA = {AMT_AVAILABLE: 10}
        goodB = {AMT_AVAILABLE: 10}
        goods = {"a": goodA, "b": goodB}
        self.assertIsNotNone(get_rand_good(goods))

    def test_transfer(self):
        goodA = {AMT_AVAILABLE: 10}
        goodB = {AMT_AVAILABLE: 10}
        trader = {"goods": {}}
        goods = {"a": goodA, "b": goodB}
        transfer(trader["goods"], goods, "a")
        self.assertEqual(goods["a"][AMT_AVAILABLE], 0)
        self.assertEqual(trader["goods"]["a"][AMT_AVAILABLE], 10)

    if __name__ == '__main__':
        main()

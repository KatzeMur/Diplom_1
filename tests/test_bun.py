from praktikum.bun import Bun
from data import BUN_NAME, BUN_PRICE


def test_bun_get_name():
    bun = Bun(BUN_NAME, BUN_PRICE)
    assert bun.get_name() == BUN_NAME


def test_bun_get_price():
    bun = Bun(BUN_NAME, BUN_PRICE)
    assert bun.get_price() == BUN_PRICE
    
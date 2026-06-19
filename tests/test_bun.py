from praktikum.bun import Bun

def test_bun_get_name():
    bun = Bun("Black bun", 100.0)
    assert bun.get_name() == "Black bun"

def test_bun_get_price():
    bun = Bun("Black bun", 100.0)
    assert bun.get_price() == 100.0

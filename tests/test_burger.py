import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

@pytest.fixture
def test_bun():
    return Bun("Black bun", 100.0)

@pytest.fixture
def test_ingredient():
    return Ingredient("SAUCE", "Hot sauce", 50.0)

@pytest.fixture
def burger():
    return Burger()

def test_set_buns(burger, test_bun):
    burger.set_buns(test_bun)
    assert burger.bun == test_bun

def test_add_ingredient(burger, test_ingredient):
    burger.add_ingredient(test_ingredient)
    assert len(burger.ingredients) == 1

@pytest.mark.parametrize("count", [1, 2, 3])
def test_add_multiple_ingredients(burger, test_ingredient, count):
    for _ in range(count):
        burger.add_ingredient(test_ingredient)
    assert len(burger.ingredients) == count

def test_remove_ingredient(burger, test_ingredient):
    burger.add_ingredient(test_ingredient)
    burger.add_ingredient(test_ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 1

def test_move_ingredient(burger, test_ingredient):
    ing1 = Ingredient("FILLING", "Meat", 100.0)
    ing2 = Ingredient("FILLING", "Cheese", 80.0)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0] == ing2

def test_get_price(burger, test_bun, test_ingredient):
    burger.set_buns(test_bun)
    burger.add_ingredient(test_ingredient)
    assert burger.get_price() == 250.0

def test_get_receipt(burger, test_bun, test_ingredient):
    burger.set_buns(test_bun)
    burger.add_ingredient(test_ingredient)
    expected = "(==== Black bun ====)\n= sauce Hot sauce =\n(==== Black bun ====)\n\nPrice: 250.0"
    assert burger.get_receipt() == expected
    
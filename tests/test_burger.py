import pytest
from praktikum.burger import Burger
from tests.test_data import EXPECTED_RECEIPT


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
    from praktikum.ingredient import Ingredient
    ing1 = Ingredient("FILLING", "Meat", 100.0)
    ing2 = Ingredient("FILLING", "Cheese", 80.0)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0] == ing2


def test_get_price(burger, test_bun, test_ingredient):
    burger.set_buns(test_bun)
    burger.add_ingredient(test_ingredient)
    expected_price = (test_bun.get_price() * 2) + test_ingredient.get_price()
    assert burger.get_price() == expected_price


def test_get_receipt(burger, test_bun, test_ingredient):
    burger.set_buns(test_bun)
    burger.add_ingredient(test_ingredient)
    assert burger.get_receipt() == EXPECTED_RECEIPT
    
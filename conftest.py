import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from tests.test_data import BUN_NAME, BUN_PRICE, INGREDIENT_TYPE, INGREDIENT_NAME, INGREDIENT_PRICE


@pytest.fixture
def test_bun():
    return Bun(BUN_NAME, BUN_PRICE)


@pytest.fixture
def test_ingredient():
    return Ingredient(INGREDIENT_TYPE, INGREDIENT_NAME, INGREDIENT_PRICE)


@pytest.fixture
def default_ingredient():
    return Ingredient(INGREDIENT_TYPE, INGREDIENT_NAME, INGREDIENT_PRICE)


@pytest.fixture
def burger():
    from praktikum.burger import Burger
    return Burger()

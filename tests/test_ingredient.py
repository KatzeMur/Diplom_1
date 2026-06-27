import pytest
from praktikum.ingredient import Ingredient
from data import INGREDIENT_TYPE, INGREDIENT_NAME, INGREDIENT_PRICE


@pytest.mark.parametrize("ing_type, name, price", [
    (INGREDIENT_TYPE, INGREDIENT_NAME, INGREDIENT_PRICE),
    ("FILLING", "Meat", 150.0),
])
def test_ingredient_creation(ing_type, name, price):
    ingredient = Ingredient(ing_type, name, price)
    assert ingredient.get_type() == ing_type

def test_ingredient_get_name(default_ingredient):
    assert default_ingredient.get_name() == INGREDIENT_NAME

def test_ingredient_get_price(default_ingredient):
    assert default_ingredient.get_price() == INGREDIENT_PRICE
    
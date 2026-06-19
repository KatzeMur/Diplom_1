import pytest
from praktikum.ingredient import Ingredient

@pytest.fixture
def default_ingredient():
    return Ingredient("SAUCE", "Hot sauce", 50.0)

@pytest.mark.parametrize("ing_type, name, price", [
    ("SAUCE", "Hot sauce", 50.0),
    ("FILLING", "Meat", 150.0),
])
def test_ingredient_creation(ing_type, name, price):
    ingredient = Ingredient(ing_type, name, price)
    assert ingredient.get_type() == ing_type

def test_ingredient_get_name(default_ingredient):
    assert default_ingredient.get_name() == "Hot sauce"

def test_ingredient_get_price(default_ingredient):
    assert default_ingredient.get_price() == 50.0

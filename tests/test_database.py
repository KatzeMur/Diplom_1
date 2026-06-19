import pytest
from unittest.mock import patch
from praktikum.database import Database

@patch('praktikum.database.Ingredient')
@patch('praktikum.database.Bun')
def test_database_init(mock_bun, mock_ingredient):
    db = Database()
    assert mock_bun.call_count == 3
    assert mock_ingredient.call_count == 6

def test_available_buns():
    db = Database()
    buns = db.available_buns()
    assert len(buns) == 3

def test_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6
    
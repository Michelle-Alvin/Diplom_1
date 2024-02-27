import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:
    @pytest.mark.parametrize("type_ing, name, price", [
        [INGREDIENT_TYPE_SAUCE, "Ketchup", 90.9],
        [INGREDIENT_TYPE_FILLING, "Salad", 20.0]
    ])
    def test_get_type(self, type_ing, name, price):
        ingredient = Ingredient(type_ing, name, price)

        assert ingredient.get_type() == type_ing

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Ketchup", 90.9)

        assert ingredient.get_name() == "Ketchup"

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Ketchup", 90.9)

        assert ingredient.get_price() == 90.9

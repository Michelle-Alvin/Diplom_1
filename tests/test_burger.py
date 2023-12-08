from unittest.mock import Mock
from unittest.mock import patch

import pytest

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture(scope="function")
def burger():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_name.return_value = "default bun"
    mock_bun.get_price.return_value = 9.00
    burger.set_buns(mock_bun)

    mock_ingredient1 = Mock()
    mock_ingredient1.get_price.return_value = 10
    mock_ingredient1.get_name.return_value = "tomato"
    mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
    burger.add_ingredient(mock_ingredient1)

    mock_ingredient2 = Mock()
    mock_ingredient2.get_price.return_value = 15
    mock_ingredient2.get_name.return_value = "salad"
    mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
    burger.add_ingredient(mock_ingredient2)

    return burger


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "dark bun"
        mock_bun.get_price.return_value = 9.99

        burger.set_buns(mock_bun)

        assert burger.bun.get_name() == "dark bun"
        assert burger.bun.get_price() == 9.99

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 10.0
        mock_ingredient.get_name.return_value = "tomato"
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_price() == 10.0
        assert burger.ingredients[0].get_name() == "tomato"

    def test_remove_ingredient(self, burger):
        assert len(burger.ingredients) == 2
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1

    def test_move_ingredient(self, burger):
        nod = burger.ingredients[1]
        burger.move_ingredient(1, 0)

        assert nod == burger.ingredients[0]
        assert nod != burger.ingredients[1]

    def test_get_price(self, burger):
        price = burger.get_price()

        assert round(price, 2) == 43.0

    @patch('praktikum.burger.Burger.get_price', return_value=43.0)
    def test_get_receipt(self, mock_get_price, burger):
        receipt = burger.get_receipt()
        expected_receipt = "(==== default bun ====)\n"
        expected_receipt += "= filling tomato =\n"
        expected_receipt += "= filling salad =\n"
        expected_receipt += "(==== default bun ====)\n\n"
        expected_receipt += "Price: 43.0"

        assert receipt == expected_receipt

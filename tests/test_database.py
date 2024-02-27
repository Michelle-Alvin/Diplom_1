from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        res = database.available_buns()

        assert res[0].get_name() == "black bun"

    def test_available_ingredients(self):
        database = Database()
        res = database.available_ingredients()

        assert res[2].get_name() == "chili sauce"
        assert res[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert res[2].get_price() == 300

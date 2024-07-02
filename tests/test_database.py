from praktikum.praktikum import Database
class TestDatabase:
    def test_bun_from_database_get_name(self):
        database = Database()
        buns_list = database.available_buns()
        assert buns_list[0].get_name() == 'black bun'
    def test_bun_from_database_get_price(self):
        database = Database()
        buns_list = database.available_buns()
        assert buns_list[0].get_price() == 100

    def test_ingredient_from_database_get_name(self):
        database = Database()
        ingredients_list = database.available_ingredients()
        current_ingredient = ingredients_list[1]
        assert current_ingredient.get_name() == 'sour cream'

    def test_ingredient_from_database_get_type(self):
        database = Database()
        ingredients_list = database.available_ingredients()
        current_ingredient = ingredients_list[5]
        assert current_ingredient.get_type() == 'FILLING'

    def test_ingredient_from_database_get_price(self):
        database = Database()
        ingredients_list = database.available_ingredients()
        current_ingredient = ingredients_list[4]
        assert current_ingredient.get_price() == 200

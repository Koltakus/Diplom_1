from praktikum import ingredient_types
from praktikum.praktikum import Ingredient
from praktikum.praktikum import Database


# В тест-сете присутсвуют тесты на проверку получения данных из базы данных
class TestIngredients:

    def test_ingredient_get_name(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE,
                                'Соус традиционный галактический',
                                15)
        assert ingredient.get_name() == 'Соус традиционный галактический'

    def test_ingredient_get_type(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE,
                                'Соус Spicy-X',
                                90)
        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_SAUCE

    def test_ingredient_get_price(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE,
                                'Соус фирменный Space Sauce',
                                80)
        assert ingredient.get_price() == 80




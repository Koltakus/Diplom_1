from praktikum.praktikum import Bun




class TestBuns:

    def test_bun_get_name(self):
        bun = Bun('Флюоресцентная булка', 988)
        assert bun.get_name() == 'Флюоресцентная булка'

    def test_bun_get_price(self):
        bun = Bun('Краторная булка', 1255)
        assert bun.get_price() == 1255






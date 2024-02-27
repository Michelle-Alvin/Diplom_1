from praktikum.bun import Bun


class TestBun:
    def test_create_bun(self):
        bun = Bun("August", 90.9)

        assert bun.get_name() == "August"
        assert bun.get_price() == 90.9

    def test_get_name(self):
        bun = Bun("TestName", 10.0)

        assert bun.get_name() == "TestName"

    def test_get_price(self):
        bun = Bun("DefaultName", 99.99)

        assert bun.get_price() == 99.99

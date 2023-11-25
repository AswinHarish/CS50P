from bank import value


def main():
    test_value_hello()
    test_value_h()
    test_value_others()


def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0


def test_value_h():
    assert value("how") == 20
    assert value("hey") == 20


def test_value_others():
    assert value("sup") == 100
    assert value("yo") == 100


if __name__ == "__main__":
    main()

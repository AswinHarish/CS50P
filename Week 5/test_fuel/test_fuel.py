from pytest import raises
from fuel import convert, gauge


def main():
    test_guage()
    test_convert()


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0


def test_zero_division():
    with raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with raises(ValueError):
        convert("3/2")


if __name__ == "__name__":
    main()

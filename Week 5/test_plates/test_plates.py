from plates import is_valid


def main():
    test_is_valid_two_letters()
    test_is_valid_length()
    test_is_valid_numbers_in_middle()
    test_is_valid_special_characters()


def test_is_valid_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("23NEW") == False
    assert is_valid("!HELLO") == False
    assert is_valid("HELLO") == True


def test_is_valid_length():
    assert is_valid("H") == False
    assert is_valid("PLATES23") == False
    assert is_valid("HELLO") == True


def test_is_valid_numbers_in_middle():
    assert is_valid("CS05AC") == False
    assert is_valid("HEL22B") == False
    assert is_valid("CSHE89") == True
    assert is_valid("HELL09") == False


def test_is_valid_special_characters():
    assert is_valid("HEL O") == False
    assert is_valid("CS,50") == False
    assert is_valid("HELL@09") == False


if __name__ == "__name__":
    main()

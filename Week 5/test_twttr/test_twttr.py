from twttr import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("just setting up my twitter") == "jst sttng p my twttr"
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("H3Ll0 WoR7D") == "H3Ll0 WR7D"
    assert shorten(".,!@?") == ".,!@?"


if __name__ == "__main__":
    main()

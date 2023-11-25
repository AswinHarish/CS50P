def main():
    word = input("Greeting: ").strip()
    value(word)
    print(f"${value(word)}")


def value(greeting):
    if "hello" in greeting.casefold():
        return 0
    elif greeting[0] in ["h", "H"]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        a, b = generate_integer(level)
        chance = 3
        while True:
            if chance >= 1:
                try:
                    ans = int(input(f"{a} + {b} = "))
                    if a + b == ans:
                        score += 1
                        break
                    else:
                        raise ValueError
                except (ValueError, NameError):
                    print("EEE")
                    chance -= 1
                    pass
            else:
                print(f"{a} + {b} = {a + b}")
                break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
    elif level == 2:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    else:
        a = random.randint(100, 999)
        b = random.randint(100, 999)

    return a, b


if __name__ == "__main__":
    main()

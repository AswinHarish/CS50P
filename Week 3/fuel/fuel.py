def percentage(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
            if x <= y:
                return x / y * 100
        except (ValueError, ZeroDivisionError):
            pass


def main():
    x = round(percentage("Fraction: "))
    if x <= 1:
        print("E")
    elif x >= 99:
        print("F")
    else:
        print(f"{x}%")


main()

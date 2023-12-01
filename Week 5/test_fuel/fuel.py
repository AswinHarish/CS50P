def main():
    fraction = input("Fraction: ")
    value = convert(fraction)
    print(gauge(value))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x <= y:
            return round(x / y * 100)
        elif y == 0:
            raise ZeroDivisionError
        else:
            raise ValueError
    except (ValueError, ZeroDivisionError) as e:
        raise e


def gauge(percentage):
    if percentage <= 1:
        return ("E")
    elif percentage >= 99:
        return ("F")
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()

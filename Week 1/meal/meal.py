def main():
    inp = input("What time is it? ")
    time = convert(inp)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    x, y = time.split(":")
    hour = float(x)
    mins = float(y) / 60
    return hour + mins


if __name__ == "__main__":
    main()

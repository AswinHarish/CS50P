import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    else:
        menu(sys.argv[1])


def menu(filename):
    try:
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
            if data:
                print(tabulate(data, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

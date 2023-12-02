import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        scourgify(sys.argv[1], sys.argv[2])


def scourgify(infile, outfile):
    try:
        with open(infile, "r") as infile:
            reader = csv.DictReader(infile)
            with open(outfile, "w") as outfile:
                header = ["first", "last", "house"]
                writer = csv.DictWriter(outfile, fieldnames=header)
                writer.writeheader()

                for student in reader:
                    lname, fname = student["name"].split(",")
                    house = student["house"]
                    writer.writerow({"first": fname.lstrip(), "last": lname, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {infile}")


if __name__ == "__main__":
    main()

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date: ")

    try:
        if "/" in date:
            month, day, year = date.split("/")
        elif "," in date:
            date = date.replace(",", "")
            month, day, year = date.split(" ")
            month = months.index(month.title()) + 1
        else:
            continue

        month = int(month)
        year = int(year)
        day = int(day)

        if 1 <= day <= 31 and 1 <= month <= 12:
            print(f"{year}-{month:02}-{day:02}")
            break
    except ValueError:
        pass

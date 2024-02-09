class Month:
    name: str
    days: int


def showday(daynumber: int, isleapyear: bool) -> (str, int):
    """Shows the month and day for a given day number.

    daynumber: a day number within the year.
    isleapyear: True if the year is a leap year.

    Returns the month and day,
    raises ValueError if daynumber is invalid.
    """

    months = (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "November",
        "December",
    )

    days = [31 for month in months]

    # Let's see, 30 days hath September...

    thirtylist = ("April", "June", "September", "November")

    for j in [months.index(k) for k in thirtylist]:
        days[j] = 30

    # Fix up February also

    days[months.index("February")] = 28 + isleapyear

    """ daymap consists of 12 Month objects, each of which has a name/days pair in it
    """

    daymap = []

    for i in range(len(months)):
        NewMonth = Month()
        NewMonth.name = months[i]
        NewMonth.days = days[i]
        daymap.append(NewMonth)

    if daynumber > 0:
        for el in daymap:
            if daynumber < el.days:
                return el.name, daynumber
            daynumber = daynumber - el.days
    raise ValueError("daynumber")


print(showday(1, False))

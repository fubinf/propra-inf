import dataclasses


@dataclasses.dataclass
class Month:
    name: str
    days: int

    def __repr__(self):
        return f"{self.name}({self.days})"


def showday(daynumber: int, isleapyear: bool) -> (str, int):
    """
    Returns the month and day for a given day number.
    daynumber: a day number within the year.
    isleapyear: True if the year is a leap year.
    Returns the month name and day,
    raises ValueError if daynumber is invalid.
    """
    monthnames = (
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
    )
    days = [31 for month in monthnames]  # assume all months have 31 days
    thirtylist = ("April", "June", "September", "November")
    for idx in [monthnames.index(thismonth) for thismonth in thirtylist]: # fix 30-day months
        days[idx] = 30
    days[monthnames.index("February")] = 28 + isleapyear  # fix February
    months = [Month(name=monthnames[i], days=days[i]) for i in range(len(monthnames))]  # our target data structure
    # now do the computation:
    if daynumber > 0:
        for month in months:
            if daynumber < month.days:  # the right month
                return month.name, daynumber
            daynumber = daynumber - month.days  # not the right month, subtract it and continue
    raise ValueError("invalid daynumber")

print(showday(1, False))
from movie_rental import Customer, Rental, Movie


def tests():
    customer = Customer("Bob")
    customer.addRental(Rental(Movie("Jaws", Movie.REGULAR), 2))
    customer.addRental(Rental(Movie("Golden Eye", Movie.REGULAR), 3))
    customer.addRental(Rental(Movie("Short New", Movie.NEW_RELEASE), 1))
    customer.addRental(Rental(Movie("Long New", Movie.NEW_RELEASE), 2))
    customer.addRental(Rental(Movie("Bambi", Movie.CHILDRENS), 3))
    customer.addRental(Rental(Movie("Toy Story", Movie.CHILDRENS), 4))

    expected = "Rental Record for Bob\n"
    expected += "\tJaws\t2.0\n"
    expected += "\tGolden Eye\t3.5\n"
    expected += "\tShort New\t3.0\n"
    expected += "\tLong New\t6.0\n"
    expected += "\tBambi\t1.5\n"
    expected += "\tToy Story\t3.0\n"
    expected += "Amount owed is 19.0\n"
    expected += "You earned 7 frequent renter points"

    assert expected == customer.statement()

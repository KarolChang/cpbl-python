def getPreviousYears(the_year: int, previous_years: int):
    return [the_year - i for i in range(previous_years)]

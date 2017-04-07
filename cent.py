import math

def centuryFromYear(year):
    return math.floor((year - 1) / 100) + 1

    # century = math.floor((year -1) / 100)+1
    # if century in range(1, 1001):
    #     return century
    # elif century in range(1001, 1901):
    #     return century
    # elif century in range(1901, 2001):
    #     return math.floor(year / 100)+ 1


print(centuryFromYear(1001))

__author__ = 'klex'

def checkio(number):
    vysledek = 1
    for i in str(number):
        if i != "0":
            vysledek = vysledek * int(i)
    return vysledek


print(checkio(123405))


def checkio(number):
    """
    Convert into the string and iterate.
    """
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res
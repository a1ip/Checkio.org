__author__ = 'klex'

def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1




def checkio(*a):
    try:
        return int(*a)
    except ValueError:
        return -1





checkio("AF", 16)
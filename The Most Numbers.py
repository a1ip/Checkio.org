__author__ = 'klex'


#moje reseni :/

def checkio(*args):
    if len(args) == 0:
        return 0
    else:
        minim = min(args)
        maxim = max(args)
        return maxim-minim


#takhle to ma vypadat
def checkio(*args):
    return max(args) - min(args) if args else 0





checkio(1, 2, 3)
checkio(5, -5)
checkio(10.2, -2.2, 0, 1.1, 0.5)
checkio()
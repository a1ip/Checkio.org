__author__ = 'klex'


def checkio(number):
    count = 0
    x = bin(number)
    for i in range(2,len(x)):
        if x[i] == '1':
            count += 1


    return count





def checkio(number):
    return bin(number).count('1')


checkio(4)
checkio(1022)
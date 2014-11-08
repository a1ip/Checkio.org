__author__ = 'klex'

def checkio(first, second):
    vysledek = []
    vysl = ""
    x = first.split(",")
    y = second.split(",")
    for word1 in x:
        if word1 in y:
            vysledek.append(word1)
            vysledek.sort()

    vysl = ','.join(vysledek)

    return vysl

def checkio(first, second):
    same_words = set(first.split(',')).intersection(second.split(','))
    return ','.join(sorted(same_words))

def checkio(first, second):
    first_set = set(first.split(","))
    second_set = set(second.split(","))

    return ",".join(sorted(first_set & second_set))


checkio("hello,world", "hello,earth")
checkio("one,two,three", "four,five,six")
checkio("one,two,three", "four,five,one,two,six,three")
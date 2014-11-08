__author__ = 'klex'

def checkio(words_set):

    if len(words_set) == 1:
        return False
    else:
        for word in words_set:
            for word1 in words_set:
                if word == word1:
                    continue
                elif word.endswith(word1):
                    return True
                else:
                    return False


def checkio(words):
    """
    You can iterate throught set.
    """
    for w1 in words:
        for w2 in words:
            if w1 != w2 and (w1.endswith(w2) or w2.endswith(w1)):
                return True
    return False



checkio({"hello", "lo", "he"})
checkio({"hello", "la", "hellow", "cow"})
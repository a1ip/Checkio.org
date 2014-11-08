__author__ = 'klex'


#moje lame solution
def checkio(words):
    count = 0
    word = words.split(" ")
    for i in range(0,len(word)):
        if not word[i].isdigit():
            count += 1
            if count == 3:
                return True
        else:
            count = 0

    return False


#kratsi solution z checkio webu :)

def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False







checkio("Hello World hello") == True, "Hello"
checkio("He is 123 man") == False, "123 man"
checkio("1 2 3 4") == False, "Digits"
checkio("bla bla bla bla") == True, "Bla Bla"
checkio("Hi") == False, "Hi"

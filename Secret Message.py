__author__ = 'klex'

#moje lame solution
def find_message(text):
    all = ""
    for i in range(len(text)):
        if text[i].isupper():
            all += text[i]
    return all

#profi solution :)
def find_message(text):
    return ''.join(c for c in text if c.isupper())




find_message("How are you? Eh, ok. Low or Lower? Ohhh.")
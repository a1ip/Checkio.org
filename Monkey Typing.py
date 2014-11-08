__author__ = 'klex'
def count_words(text, words):
    count = 0
    for i in words:
        if i in text.lower():
            count += 1
    print(count)
    return count



    #These "asserts" using only for self-checking and not necessary for auto-testing
count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                      {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

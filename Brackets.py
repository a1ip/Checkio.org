__author__ = 'klex'


def checkio(data):
    stack = [""]
    brackets = {"(": ")", "[": "]", "{": "}"}
    for c in data:
        if c in brackets:
            stack.append(brackets[c])
        elif c in brackets.values() and c != stack.pop():
            return False
    return stack == [""]


#checkio("[1+1]+(2*2)-{3/3}")
#checkio("(({[(((1)-2)+3)-3]/3}-3)")
#checkio("(3+{1-1)}")
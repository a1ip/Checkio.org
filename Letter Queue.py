__author__ = 'klex'

push = 'PUSH '
pop = 'POP'

def letter_queue(commands):
    vysl = ""
    for i in range(len(commands)):
        if push in commands[i]:
            vysl += commands[i].replace((push),"")
        else:
            vysl = vysl[1:]
    return vysl


letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"])
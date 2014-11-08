__author__ = 'klex'

#moje shitka

ous = "OOO"
exes = "XXX"


def checkio(game_result):
    game_result2 = list(zip(*game_result))
    if game_result[0][0] == 'O' and game_result[1][1] == 'O' and game_result[2][2] == 'O':
        return "O"
    if game_result[0][0] == 'X' and game_result[1][1] == 'X' and game_result[2][2] == 'X':
        return "X"
    if game_result[0][2] == 'O' and game_result[1][1] == 'O' and game_result[2][0] == 'O':
        return "O"
    if game_result[0][2] == 'X' and game_result[1][1] == 'X' and game_result[2][0] == 'X':
        return "X"
    for i in range(3):
        if game_result[i] == ous:
            return "O"
        if game_result[i] == exes:
            return "X"
        if "".join(game_result2[i]) == ous:
            return "O"
        if "".join(game_result2[i]) == exes:
            return "X"
    return "D"


#imba reseni

def checkio(game_result):
    def check(s):
        matrix = game_result
        if (s * 3) in matrix or (s * 3) in [''.join(x) for x in zip(*matrix)]:
            return s
        if matrix[0][0] == matrix[1][1] == matrix[2][2] == s:
            return s
        if matrix[0][2] == matrix[1][1] == matrix[2][0] == s:
            return s
        return False
    return check('X') or check('O') or 'D'




checkio(["X.O","XX.","XOO"])
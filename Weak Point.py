__author__ = 'klex'

#moje reseni
def weak_point(matrix):
    matrix2 = list(zip(*matrix))
    nejmensi_radek = []
    nejmensi_sloupec = []
    for i in range(len(matrix)):
        nejmensi_radek.append(sum(matrix[i]))
        nejmensi_sloupec.append(sum(matrix2[i]))
    return [nejmensi_radek.index(min(nejmensi_radek)), nejmensi_sloupec.index(min(nejmensi_sloupec))]


#nebo

def weak_point(matrix):
    n = len(matrix)
    row = min(range(n), key=lambda r:sum(matrix[r][c] for c in range(n)))
    col = min(range(n), key=lambda c:sum(matrix[r][c] for r in range(n)))
    return row, col


#nebo

def find_week_row(matrix):
    return min((sum(line), r) for r, line in enumerate(matrix))[1]

def weak_point(matrix):
    return find_week_row(matrix), find_week_row(zip(*matrix))

weak_point([[7, 2, 7, 2, 8],
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]])
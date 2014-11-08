__author__ = 'klex'


def find_week_row(matrix):
    return min((sum(line), r) for r, line in enumerate(matrix))[1]


def weak_point(matrix):
    return find_week_row(matrix), find_week_row(zip(*matrix))



weak_point([[7, 2, 7, 2, 8],
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]])
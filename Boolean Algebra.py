__author__ = 'klex'

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == "conjunction":
        return (x and y)
    if operation == "disjunction":
        return (x or y)
    if operation == "implication":
        return not(x) or y
    if operation == "exclusive":
        return (x ^ y)
    if operation == "equivalence":
        if (x == y):
            return True
        else:
            return False




def boolean(x, y, operation):
    if operation == "conjunction": return x & y
    if operation == "disjunction": return x | y
    if operation == "implication": return (1 ^ x) | y
    if operation == "exclusive":   return x ^ y
    if operation == "equivalence": return x ^ y ^ 1
    return 0
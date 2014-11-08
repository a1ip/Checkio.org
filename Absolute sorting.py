__author__ = 'klex'

#moje "coool" reseni
#def checkio(numbers_array):
#    s = []
#    neg = []
 #   for i in numbers_array:
 #       s.append(abs(i))
#        if i < 0:
#            neg.append(i)
#    s.sort()
#    for i in range(len(neg)):
 #       for y in range(len(s)):
 #           if abs(neg[i]) == s[y]:
 #               s.pop(y)
 #               s.insert(y,neg[i])
 #   return s


#takhle to ma vypadat :DDD

def checkio(numbers_array):
    return print(sorted(numbers_array, key=abs))



checkio((-20, -5, 10, 15))

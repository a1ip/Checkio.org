__author__ = 'klex'


def count_inversion(s):
        count = 0
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if s[i] > s[j]:
                    print(s[i], ">", s[j])
                    count += 1
        return count

print(count_inversion((1,2,5,3,4,7,6)))
print(count_inversion((0, 1, 2, 3)))
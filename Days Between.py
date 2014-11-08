__author__ = 'klex'
import datetime

#moje reseni
def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    a = datetime.date(date1[0],date1[1],date1[2])
    b = datetime.date(date2[0],date2[1],date2[2])

    return abs(a-b).days





from datetime import datetime

def days_diff(date1, date2):
    return abs((datetime(*date1)-datetime(*date2)).days)


days_diff((1982, 4, 19), (1982, 4, 22))
days_diff((2014, 1, 1), (2014, 8, 27))
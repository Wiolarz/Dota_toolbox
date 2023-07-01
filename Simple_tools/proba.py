""""""
''' Przeszukiwanie pliku '''
import sys
import statistics
dd = []
co = '#'
f = open('Pick.txt', 'r')
linie = f.readlines()
f.close()
for linia in linie:
    if not co in linia:
        linia = linia.replace("\n", "")
        dd.append(float(linia))
        #print (linia)


def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def stddev(data, ddof=0):
    """Calculates the population standard deviation
    by default; specify ddof=1 to compute the sample
    standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/(n-ddof)
    return pvar**0.5

e1 = []
e2 = []

e3 = []
e4 = []

e5 = []


for i in range(119):
    e1.append(dd[i])
    e2.append(dd[i + 119])
    e3.append(dd[i + 238])
    e4.append(dd[i + 357])
    e5.append(dd[i + 476])

print("wszystkie rangi")
print(statistics.stdev(dd))
print("Niskie")
print(statistics.stdev(e1))
print("Archont")
print(statistics.stdev(e2))
print("Legend")
print(statistics.stdev(e3))
print("Ancient")
print(statistics.stdev(e4))
print("Wysokie")
print(statistics.stdev(e5))
#, sum(e5) / len(e5)
'''
a = 1
b = 1
c = 1

for i in range(119):
    a *= float(dd[i])

print(a)
a = a / 119
print(a)

for i in range(119, 236):
    b *= float(dd[i])

print(b)
b = b / 119
print(b)

for i in range(236, 355):
    c *= float(dd[i])

print(c)
c = c / 119
print(c)
'''
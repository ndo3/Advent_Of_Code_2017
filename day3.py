##
# Although you don't know who I am and sorry for being a creep, thanks
# Zak Wagweiser for enlightening me with how to solve this problem! And
# just generally cool tools from Python that I can apply in the future
##

##
# What I learned: collections, defaultdict, sum(), Manhattan Distance
# Also itertools, count(), hell yeaaa!! Also _!
# I still don't have a good answer for this problem yet rip yikes
##

from itertools import count
from collections import defaultdict

def create_spiral():
    array, x, y = defaultdict(int), 0, 0
    array[0,0] = 1
    sn = lambda x,y: sum(array[k,l] for k in range(x-1, x+2) for l in range(y-1, y+2))

    for s in count(1,2):
        for _ in range(s): x+= 1; array[x,y] = sn(x,y); yield array[x,y]
        for _ in range(s): y-= 1; array[x,y] = sn(x,y); yield array[x,y]
        for _ in range(s+1): x-= 1; array[x,y] = sn(x,y); yield array[x,y]
        for _ in range(s+1): y+= 1; array[x,y] = sn(x,y); yield array[x,y]

def calcDistance(number):
    for x in create_spiral():
        if x > number:
            return x


if __name__ == '__main__' :
    for i in range(10):
        print calcDistance(i)

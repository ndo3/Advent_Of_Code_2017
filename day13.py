from collections import defaultdict

##
# Rip long code
##

def trip_severity(string):
    lines = string.split(" \n ")
    info = defaultdict(int)
    max_depth = float("-inf")
    total_severity = 0
    posdict = []
    max_range = []
    positivedir = []
    last_depth = 0
    for line in lines:
        depth,_,therange = line.partition(": ")
        info[int(depth)] = int(therange)

        ## This is to add the positions different
        if int(depth) - 1 != last_depth:
            for hah in range(last_depth+1, int(depth)):
                info[hah] = 0
                posdict.append(0)
                positivedir.append(True)
                max_range.append(0)

        posdict.append(0)
        positivedir.append(True)
        max_range.append(int(therange))
        ## This is only to keep track of the positions difference
        last_depth = int(depth)
        ## Keeping track of the max_depth
        if int(depth) > max_depth:
            max_depth = int(depth)


    print posdict
    print positivedir
    print max_range


    curr_pos = 0
    for i in range(max_depth+1):
        if i != 0:
            curr_pos += 1
        print curr_pos
        if posdict[curr_pos] == 0 and max_range[curr_pos] != 0:
            total_severity += calcSeverity(curr_pos, max_range[curr_pos])
        j = 0
        for _ in posdict:
            if posdict[j] == 0 and max_range[j] != 0:
                positivedir[j] = True
                posdict[j] += 1
            elif posdict[j] == max_range[j]-1 and max_range[j] != 0:
                positivedir[j] = False
                posdict[j] -= 1
            elif positivedir[j] == False and max_range[j] != 0:
                posdict[j] -= 1
            elif positivedir[j] == True and max_range[j] != 0:
                posdict[j] += 1

            j += 1

    return total_severity

def calcSeverity(depth, therange):
    return depth*therange

if __name__ == '__main__' :
    print trip_severity("0: 3 \n 1: 2 \n 4: 4 \n 6: 4")

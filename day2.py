def processList(string):
    rows = string.split('\n')
    i = 0
    for row in rows:
        row = row.split()
        rows[i] = row
        i+= 1
    return rows

def checksum(array):
    the_sum = 0
    for row in array:
        smallest = float("inf")
        largest = float("-inf")
        for member in row:
            if int(member) < smallest:
                smallest = int(member)
            if int(member) > largest:
                largest = int(member)
        the_sum += (largest - smallest)
    return the_sum

if __name__ == '__main__' :
    print checksum(processList("5 1 9 5 \n 7 5 3 \n 2 4 6 8"))

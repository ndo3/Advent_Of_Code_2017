from collections import defaultdict

##
# What I learned: A better style to do array wrapping, turning arr into string
# and yes i love defaultdict
##

## My shitty solution
def distributer(list_of_banks):
    max_num = float("-inf")
    index = 0
    max_index = 0
    for num in list_of_banks:
        if num > max_num:
            max_num = num
            max_index = index
        index+= 1
    list_of_banks[max_index] = 0
    while max_num != 0:
        for i in range(max_index + 1, len(list_of_banks)):
            list_of_banks[i]+= 1
            max_num -=1
        for j in range(max_index+1):
            list_of_banks[j]+= 1
            max_num -=1
    return list_of_banks

## This is just a very beautiful practice that I want to keep note of:
def redistributer(arr, pos, total):
    if pos >= len(arr):
        pos = 0
    if total <= 0:
        return arr
    else:
        arr[pos] += 1
        return redistributer(arr, pos+1, total-1)

def arr_to_string(arr):
    return " ".join(str(x) for x in arr)

def check_num(arr):
    ## Putting stuff in
    memory = defaultdict(int)
    memory[arr_to_string(arr)] += 1
    time = 0
    ## Checking max
    while memory[arr_to_string(arr)] <= 1:
        max_value = max(arr)
        arr[arr.index(max(arr))] = 0
        arr = redistributer(arr, arr.index(max(arr)) + 1, max_value)
        memory[arr_to_string(arr)] += 1
        time += 1
    return time

if __name__ == '__main__' :
    print check_num([0,2,7,0])

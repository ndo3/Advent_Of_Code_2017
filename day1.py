def captcha(string):
    count = 0
    check = str(string)
    for i in range(len(check)):
        if i == len(check) - 1:
            com_i = 0
        else:
            com_i = i+1
        if check[i] == check[com_i] and i != com_i:
            count+=1
    return count

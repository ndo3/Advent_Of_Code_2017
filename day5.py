def num_steps(instruction):
    num_steps = 0
    pos = 0
    while pos < len(instruction):
        num_steps += 1
        tmp = pos
        pos = pos + instruction[pos]
        instruction[tmp] += 1

    return num_steps

if __name__ == '__main__' :
    print num_steps([0, 3, 0, 1, -3])

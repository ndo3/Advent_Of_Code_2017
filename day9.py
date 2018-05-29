def total_score(string):
    num_o, num_c, pt, pos, gbg_o = 0, 0, 0, 0, False
    point = process_digit(string, pos, num_o, num_c, pt, gbg_o)
    return point

def process_digit(string, pos, num_opened, num_closed, point, garbage_opened):
    if pos == len(string):
        return point
    else:
        if garbage_opened == False:
            if string[pos] == "{":
                num_opened += 1
                pos += 1
            elif string[pos] == "}":
                num_closed += 1
                pos += 1
                if num_opened >= num_closed and num_opened != 0:
                    point += 1
            elif string[pos] == "!":
                pos += 2
            elif string[pos] == "<" and garbage_opened == False:
                garbage_opened == True
                pos += 1
            else:
                pos += 1


        else:
            if the_digit == ">":
                garbage_opened == False
                pos += 1
            elif the_digit == "!":
                pos += 2


        return process_digit(string, pos, num_opened, num_closed, point, garbage_opened)


if __name__ == '__main__' :
    print total_score("{{<ab>},{<ab>},{<ab>},{<ab>}}")

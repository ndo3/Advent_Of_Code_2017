## Yikes what a question

def final_count(initA, initB, multiplier_a, multiplier_b, divider):
    final_count = 0
    num_gen = 0
    while num_gen != 40000000:
        new_arr = generate_next_number(initA, initB, multiplier_a, multiplier_b, divider)
        num_gen += 1
        boo = check_match(new_arr)
        print num_gen
        if boo:
            final_count += 1
        initA = new_arr[0]
        initB = new_arr[1]
    return final_count

def generate_next_number(oldA, oldB, multiplier_a, multiplier_b, divider):
    return [(oldA*multiplier_a)%divider, (oldB*multiplier_b)%divider]

def check_match(int_arr):
    a = int_to_bin(int_arr[0])
    b = int_to_bin(int_arr[1])
    if len(a) < 16 or len(b) < 16:
        return False
    count_same = 0
    for i in range(16):
        if a[len(a)-i-1] != b[len(b)-i-1]:
            return False
        else:
            count_same += 1
    return True

##
# This is such beautiful code
##
def int_to_bin(num):
    if num == 0:
        return "0"
    bin_s = ""
    while num: # Learned that & 1 is the lowest bit
        if num & 1 == 1:
            bin_s = "1" + bin_s
        else:
            bin_s = "0" + bin_s
        num /= 2
    return bin_s

if __name__ == '__main__' :
    print final_count(65, 8921, 16807, 48271, 2147483647)

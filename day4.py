##
# What I learned: System and learning how to read stuff from the system
##

import sys
from collections import defaultdict

## This is the method with the file passed from the system
def num_valid_passphrase():
    valid_num = 0
    dict_store = defaultdict(int)
    for passcode in sys.stdin: #sys.stdin read each line in the input file
        groups = passcode.split() # Splitting the spaces
        for group in groups:
            dict_store[group] += 1
            if dict_store[group] > 1:
                break;
        valid_num += 1
    return valid_num

## This is a slightly modified version so I can check easily
def num_valid_passphrase_test(passlist):
    valid_num = 0
    for passcode in passlist: #sys.stdin read each line in the input file
        dict_store = defaultdict(int)
        valid = True
        groups = passcode.split() # Splitting the spaces
        for group in groups:
            dict_store[group] += 1
            if dict_store[group] > 1:
                valid = False
                break;
        if valid:
            valid_num += 1
    return valid_num

import sys
import operator ## Yes I learned this!

####
# What I learned: operator, the use of {}. I also sneaked onto the internet
# to learn about different interesting Python modules, and the list is:
# nose, matplotlib, grab, MechanicalSoup, Selenium, requests, peewee, pygame
# PrettyTable, progressbar, uuid
####
# Additionally, these are the modules that were supposed to be cool:
# Beautifulsoup, Requests (Talking to a webserver), Oset (ordered set)
# Defaultdict, Argparse (to print error messages and exit), boltons (check out)
# Numpy (matrix and array computations), Scikit-learn (easy to use machine learning)
# PyToolz (addition for functional programming, iterators, functions and dicts)
# Pandas (Supposed to be very good at data analysis), Seaborn (graph rep)
# SQLAlchemy (Database Library), Twisted (network application development)
# SciPy (library of algorithms and mathematical tools), Pyglet (3D animation engine)
# MySQLdb, PyGreSQL, mechanize
#
#
####

def answer(string):
    data = string.split(" \n ")
    registers, registers_value= [], []
    command = {"<": operator.lt, ">": operator.gt, "<=": operator.le, ">=": operator.ge, "!=": operator.ne, "==": operator.eq}
    op = {"inc": operator.add, "dec": operator.sub}
    max_val = float("-inf")
    for line in data:
        if len(line) != 0:
            inp = line.split()
            ## This part is to register all the registers into the array
            register = inp[0]
            registers.append(register)
            registers_value.append(0)

    for line in data:
        if len(line) != 0:
            cmd = line.split()
            #print cmd
            if command[cmd[5]](registers_value[registers.index(cmd[4])], int(cmd[6])):
                registers_value[registers.index(cmd[0])] = op[cmd[1]](registers_value[registers.index(cmd[0])], int(cmd[2]))


    return max(registers_value)

if __name__ == '__main__' :
    print answer("b inc 5 if a > 1 \n a inc 1 if b < 5 \n c dec -10 if a >= 1 \n ")

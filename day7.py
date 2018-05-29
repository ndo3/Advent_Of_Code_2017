import sys

class Program(object):

    def __init__(self, key, value, children, balanced = True):
        self.key = key
        self.value = value
        self.children = children
        self.balanced = balanced

## Learned: re.split() python ## The use of | in Python
## Learned: data .find() method ## The difference between append and extend
## Learned: Partition method

def process_data():
    data = sys.stdin.readlines()
    programlist = []
    childlist = []
    for line in data:
        value = line[line.find("(")+1 : line.find(")")]
        key,_,_ = line.partition(" ") # nice use of _
        _,_,lastarg = s.partition(" -> ") # nice use of _
        children = re.split(" |, |\n", lastarg)
        programlist.append(Program(key, value, children))
        childlist.extend(children) # nice use of extend

    bottom_program = None
    for program in programlist:
        for child in childlist:
            if program == child:
                break;
        bottom_program = program

    #########
    # Input would be:
    # pbga (66)
    # xhth (57)
    # ebii (61)
    # havc (66)
    # ktlj (57)
    # fwft (72) -> ktlj
    # qoyq (66)
    # padx (45) -> pbga, havc, qoyq
    # tknk (41) -> ugml, padx, fwft
    # jptl (61)
    # ugml (68) -> gyxo, ebii, jptl
    # gyxo (61)
    # cntj (57)
    ##########

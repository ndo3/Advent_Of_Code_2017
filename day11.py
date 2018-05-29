##
# With this, I basically learned more about hexagons and hexagonal grids
# in Computer Science, and I found a link here which is really interesting
# in case anyone want to check out:
# https://www.redblobgames.com/grids/hexagons/
##

def shortest_num_steps(arr_steps):
    ## This is to keep track of the change in 3D - x, y and z
    dx = 0
    dy = 0
    dz = 0
    steps = []
    for step in arr_steps:
        if step == "n":
            dy += 1
            dz -= 1
        elif step == "s":
            dy -= 1
            dz += 1
        elif step == "ne":
            dx += 1
            dz -= 1
        elif step == "nw":
            dx -= 1
            dy += 1
        elif step == "se":
            dx += 1
            dy -= 1
        elif step == "sw":
            dx -= 1
            dz += 1

    return (abs(dx) + abs(dy) + abs(dz))/2


def process_list(path):
    return path.split(",")

if __name__ == '__main__' :
    print shortest_num_steps(process_list("se,sw,se,sw,sw"))

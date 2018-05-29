def process_list(string):
    lines = string.split(" \n ")
    graph = {}
    nodes = []
    num_nodes = 0
    for line in lines:
        num_nodes += 1
        node,_,reach_node = line.partition(" <-> ")
        ind_node = reach_node.split(", ")
        node = int(node)
        nodes.append[node]
        ind_node = map(lambda x: int(x), ind_node)

        for each in ind_node:
            if node not in graph:
                graph[node] = []
            if each not in graph:
                graph[each] = []
            graph[node].append(each)
            graph[each].append(node)

    num_groups = 0

    for i in range(num_nodes):
        queue = []
        visited = []
        if i == 0:
            queue.append(i)
        cur_node = queue.pop()
        for con_node in graph[node[i]]:
            if con_node not in visited:
                visited.append(con_node)
                queue.append(con_node)

        queue = [x for x in queue if x not in visited]
        num_groups += 1

    return num_groups

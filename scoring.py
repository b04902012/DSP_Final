datatype = __import__('datatype')
graph = datatype.graph
node = datatype.node

def redundancy(g, p): #g = graph, p = path
    intersect = [r[0] for r in g.get_pri(p[0])]
    for i in p[1:]:
        pri_list = [r[0] for r in g.get_pri(i)]
        ite = intersect
        for j in ite:
            if j not in pri_list:
                intersect.remove(j)
    return len(intersect)

def scoring_simple(g, p): #g = graph, p = path
    length = len(p)
    sum_of_redundancy = 0.0
    for i in range(length):
        for k in range(i+1, length):
            sum_of_redundancy += (redundancy(g, p[i:k+1]) * (k-i+1))
    return sum_of_redundancy / length



datatype=__import__('datatype')
node=datatype.node
graph=datatype.graph
def start_node(g,s,t):
    return (g.get_avg_order(s)<t)
    


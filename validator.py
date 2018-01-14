datatype=__import__('datatype')
node=datatype.node
graph=datatype.graph
start_node=__import__('start_node').start_node
end_node=__import__('end_node').end_node
def valid(g,p,t):
    return start_node(g,p.t) and end_node(g,p)

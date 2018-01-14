start_node=__import__('start_node').start_node
end_node=__import__('end_node').end_node


def traversal(g):
    path_list=[]
    def traval(g,s,p):
        if(end_node(g,s)):
            path_list.append(p.append(s))
            return
        for s2 in g.nodes[s].next:
            if(not g.visited(s2)):
                g.visit(s2)
                traval(g,s2,p.append(s2),pl)
                g.unvisit(s2)

    for s,v in g.nodes.items():
        if(start_node(g,s,5)):
            traval(g,s,[])
    return path_list

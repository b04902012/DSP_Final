start_node=__import__('start_node').start_node
end_node=__import__('end_node').end_node
redundancy=__import__('scoring').redundancy


def traversal(g):
    path_list=[]
    def traval(g,s,pp):
        if(len(pp)>20):
            return
        p=pp[0:]
        if(end_node(g,s)):
            p.append(s)
            path_list.append(p)
            return
        for s2 in g.nodes[s]['next']:
            if(not g.get_visited(s2)):
                if(redundancy(g,[s,s2])>len(g.nodes)//200):
                    g.visit(s2)
                    p.append(s)
                    traval(g,s2,p)
                    p.remove(s)
                    g.unvisit(s2)

    for s,v in g.nodes.items():
        if(start_node(g,s,5)):
            g.visit(s)
            traval(g,s,list())
            g.unvisit(s)
    return path_list

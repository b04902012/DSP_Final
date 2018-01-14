start_node=__import__('start_node').start_node
end_node=__import__('end_node').end_node
redundancy=__import__('scoring').redundancy


def traversal(g,red_thr):
    path_list=[]
    deny_list = ["VB", "CC", "VBP", "PRP", "TO", "IN", "VBD", "VBZ", "RB", "PRP$"]
    def traval(g,s,pp,red_thr):
        if(len(pp) >= 1 and redundancy(g,pp)<red_thr):
            return
        if(len(pp)>10):
            return
        p=pp[0:]
        if(end_node(g,s)):
            p.append(s)
            path_list.append(p)
            return
        for s2 in g.nodes[s]['next']:
            if(not g.get_visited(s2) and s2.split('^')[1] != 'PRP'):
                g.visit(s2)
                p.append(s)
                traval(g,s2,p,red_thr)
                p.remove(s)
                g.unvisit(s2)

    for s,v in g.nodes.items():
        print(s)
        if((s.split('^')[1] not in deny_list) and start_node(g,s,5)):
            g.visit(s)
            traval(g,s,list(),red_thr)
            g.unvisit(s)
    return path_list

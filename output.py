from similarity import similarity

datatype = __import__('datatype')
graph = datatype.graph
node = datatype.node

def output(path_score_pair, top_N, threshold):
    result = sorted(path_score_pair, reverse=True, key=lambda x : x[1])
    ans = []
    while len(result) > len(ans) and len(ans) < top_N:
        ans.append(result[len(ans)])
        ite = result[len(ans):]
        for i in ite:
            if similarity(ans[-1][0], i[0]) > threshold:
                result.remove(i)
    return ans


def dynamicArray(n, queries):
    col = [[] for i in range(n)]
    res = []
    lastanswer = 0
    for q in queries:
        q = list(map(lambda queryPart: int(queryPart), q.split(' ')))
        data = (q[1]^lastanswer)%n
        if q[0] == 1:
            col[data].append(q[2])
        elif q[0] == 2:
            ind_x = q[2]%len(col[data])
            lastanswer = col[data][ind_x]
            res.append(lastanswer)

    return res 

dynamicArray(2, [
    '1 0 5', 
    '1 1 7', 
    '1 0 3', 
    '2 1 0', 
    '2 1 1'
    ]) == [7, 3]
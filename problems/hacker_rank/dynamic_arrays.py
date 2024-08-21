arr=[[]for i in range(0,n)]
lastAnswer=0
answers=[]    
for query in queries:
    idx= (query[1]^lastAnswer)%n
    if query[0]==1:
        arr[idx].append(query[2])
    if query[0]==2:
        lastAnswer= arr[idx][query[2]% len(arr[idx])]
        answers.append(lastAnswer)
return answers

dynamicArray(2, [
    '1 0 5', 
    '1 1 7', 
    '1 0 3', 
    '2 1 0', 
    '2 1 1'
    ]) == [7, 3]
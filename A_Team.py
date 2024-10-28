def countProblems (arr):
    countDic = {'count': 0}
    for i in arr:
        if(i == 1):
            countDic['id'] = i
            countDic['count'] += 1

    return countDic


n = input()
#print(f"Print the number of test case {n}")
result = 0
for _ in range(int(n)):
    arr = list(map(int, input().split())) 
    #print(f"This is the input arr {arr}")
    #print(f"This is the result of CountProblems", countProblems(arr))
    countValues = countProblems(arr)
    if (countValues['count'] == 3 or countValues['count'] == 2 ):
        result += 1
        
#print(f"Result values is {result}")
print(int(result)) 
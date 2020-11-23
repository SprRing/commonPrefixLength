def commonPrefix(inputs):
    # Write your code here
    res = []
    for k in inputs: 
        temp = 0
        suf = ""
        for i in range(len(k)): 
            for j in range(len(k)-i):
                if k[j] != k[i:][j]:
                    temp += j
                    break
            else:
                temp += len(k)-i
            print(temp)
        res.append(temp)
    return res
    
print(commonPrefix(["abcabcd"]))


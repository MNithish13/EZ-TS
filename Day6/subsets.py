def subset(list1):
    res=[]
    subset1=[]
    def s(i=0):
        if i>=len(list1):
            res.append(subset1.copy())
            return
        subset1.append(list1[i])
        s(i+1)
        subset1.pop()
        s(i+1)
    s()
    return res
n=[1,2,3]
print(subset(n))
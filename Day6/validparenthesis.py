def p(n):
    res=[]
    stack=[]
    def subset(opencount=0,closedcount=0):
        if opencount==closedcount==n:
            res.append(''.join(stack))
        if opencount<n:
            stack.append('(')
            subset(opencount+1,closedcount)
            stack.pop()
        if opencount>closedcount:
            stack.append(')')
            subset(opencount,closedcount+1)
            stack.pop()
    subset()
    return res
n=int(input())
print(p(n))
            
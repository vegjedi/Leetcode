def isValid(s):
    l1 =['(','{','[']
    l2 =[')','}',']']
    li = list(s)
    while li != []:
        x = li[0]
        if (x not in l1) or (l2[(l1).index(x)] not in li):
            rel = False
            break
        else: 
            li.remove(x)
            li.remove(l2[l1.index(x)])
            print(li)
            if li == []:
                rel = True
                break
    return print(rel)             

for s in ["(([]){})", "([)]", "()()", "}{"]:
    print(s)
    isValid(s)
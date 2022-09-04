def isValid(s):
    n = len(s)
    if n%2 == 1:
        rel = False
    else:
        l1 =['(','{','[',')','}',']']
        l2 =['1','2','3','4','5','6']
        for x,y in zip(l1, l2):
            s = s.replace(x, y)
        print(s)
        i = 0
        while i < n-1:
            if int(s[i]) != (int(s[i+1]) - 3):
                rel = False
                break
            i += 2
            rel = True
        if rel != True:
            i = 0
            while i < int(n/2):
                if int(s[i]) != (int(s[n -1 -i]) - 3):
                    rel = False
                    break
                i += 1
                rel = True
    return print(rel)

s = "{{{{[]}}}}"

isValid(s)
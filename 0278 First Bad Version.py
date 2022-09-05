# Author: Minh
# Date: Sep5, 2022

def firstBadVersion(n):
    if n == 1:
        return n
    else:
        min, max = 1, n
        while ((max - min) > 1):
            mid = (max-min)//2
            if isBadVersion(min + mid) == False:
                min = min + mid + 1
            else:
                max = min + mid
        if isBadVersion(min):
            return min
        else:
            return max
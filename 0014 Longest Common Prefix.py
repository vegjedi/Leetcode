# Author: Minh
# Date: Sep 02 2022

def longestCommonPrefix(strs):
    if len(strs) == 1:
        output = strs[0]
    else: 
        output = ""
        sample = sorted(strs, key=len)[0]
        for x in range(len(sample)+1):
            if all(sample[0:x] == y[0:x] for y in strs):
                output = sample[0:x]
            else:
                break
    return output

strs = ["flower","flow","flight"]

longestCommonPrefix(strs)
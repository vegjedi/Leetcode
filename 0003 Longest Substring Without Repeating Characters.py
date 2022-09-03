def lengthOfLongestSubstring(s):
    def check(word):
        for z in word:
            if word.count(z) > 1:
                False
                break
        else:
            return True

    result = 0
    
    for x in range(len(s)):
        for y in range(x, len(s)+1):
            word = s[x:y]
            if check(word):
                result = max(len(word), result)
    
    return print(result)

s = 'pwwkew'

lengthOfLongestSubstring(s)


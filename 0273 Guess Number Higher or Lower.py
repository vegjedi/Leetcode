def guessNumber(n):
    if n == 1:
        return n
    else:
        min, max = 1, n
        while ((max - min) > 1):
            mid = (max-min)//2
            if guess(min + mid) == 1:
                min = min + mid + 1
            elif guess(min + mid) == -1:
                max = min + mid - 1
            else:
                min = min + mid
                break
        if guess(min) == 0:
            return min
        else:
            return max
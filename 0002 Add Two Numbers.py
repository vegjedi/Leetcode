def addTwoNumbers(l1, l2):
    finalValue = 0
    finalList = []
    for x, number in enumerate(l1):
        finalValue = finalValue + number*(10**x)
    for y, number in enumerate(l2):
        finalValue = finalValue + number*(10**y)
    for z in str(finalValue)[::-1]:
        finalList.append(int(z))
    return finalList

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

print(addTwoNumbers(l1,l2))
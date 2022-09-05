def searchInsert(nums, target):
    if target < nums[0]:
        return 0
    elif target > nums [-1]:
        return len(nums)
    else:
        for i in range(len(nums)):
            if (nums[i] < target) and (target < nums[i+1]):
                l = i
                break
            elif nums[i] == target:
                l = i + 1
                break
        return l

nums = [1,3,5,6]
target = 5

print(searchInsert(nums, target))

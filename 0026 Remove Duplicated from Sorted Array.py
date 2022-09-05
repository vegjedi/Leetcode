def removeDuplicates(nums):
    if len(nums) == 0:
        return nums
    else:
        l=[]
        dup = 0
        while len(nums) > 0:
            no = nums[0]
            dup = dup + nums.count(no) - 1
            l.append(nums[0])
            for i in range(1, nums.count(no)+1):
                nums.remove(no)
        l = l + ['_'] * dup
        return l

nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))
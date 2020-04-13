def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # if len(nums) == 1:
    #     return nums
    n = len(nums)
    k = len(nums) -1
    i = 0
    while i <= k:
        while i < n and nums[i] != 0:
            i +=1
        while k >0 and nums[k] == 0:
            k -= 1
        j = i+1
        if i < n:
            while j < n:
                nums[j-1] = nums[j]
                j += 1

            nums[j-1] = 0
            if nums[i] != 0:
                i = i+ 1
    return nums

print(moveZeroes([0,0]))

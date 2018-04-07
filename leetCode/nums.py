class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (nums == None or object == None):
            return None
        i1 = 0
        n = len(nums)
        while(i1<n-1):
            i2 = i1+1
            while(i2< n):
                sum = nums[i1] + nums[i2]
                if (sum == target):
                    return [i1, i2]
                i2 = i2+1
            i1 = i1+1
        return None


sol = Solution()
print sol.twoSum([3,2,4], 6)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num1loc = 0
        num2loc = 0
        z = 0
        sum = 0
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                sum = nums[x] + nums[y]
                if sum == target:
                    num1loc = x
                    num2loc = y
                    return[x, y]
                    
nums = [2, 5, 5, 11]
sol = Solution()

print(sol.twoSum(nums, 10))
        
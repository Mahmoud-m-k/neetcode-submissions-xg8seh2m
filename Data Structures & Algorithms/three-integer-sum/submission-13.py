class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:

                currentSum = n + nums[l] + nums[r]

                if currentSum > 0:
                    r -= 1
                elif currentSum < 0:
                    l += 1
                else:
                    ans.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans
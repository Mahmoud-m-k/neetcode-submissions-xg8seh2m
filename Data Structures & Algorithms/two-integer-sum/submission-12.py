class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = dict()
        for i in range(len(nums)):
            diff =  target - nums[i]
            if diff in tracker:
                return [tracker[diff], i]
            tracker[nums[i]] = i

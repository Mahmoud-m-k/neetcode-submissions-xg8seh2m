class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        prevMax = 0
        currMax = 0
        i = 0
        j = 0
        for i in numsSet:
            
            num = i
            prevMax = 0
            if num - 1 not in numsSet:
                while num in numsSet:
                    print(num)
                    prevMax += 1
                    num += 1
            
            if prevMax > currMax:
                currMax = prevMax

        return currMax

    
        
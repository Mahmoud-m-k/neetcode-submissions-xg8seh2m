class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxVol = 0
        prevMax = 0

        while l < r:
            minHeight = min(heights[l], heights[r])
            prevMax = (r - l) * minHeight
            maxVol = max(prevMax, maxVol)

            if heights[l] > heights[r]:
                r-=1
            else:
                l += 1
        return maxVol

       
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        l, r = 0, len(heights) - 1

        while l <= r:
            area = (r - l) * min(heights[r], heights[l])
            if area > largestArea:
                largestArea = area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return largestArea
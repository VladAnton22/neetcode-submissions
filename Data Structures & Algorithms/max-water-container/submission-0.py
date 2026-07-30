class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = abs(j - i) * min(heights[i], heights[j])
                if area > largestArea:
                    largestArea = area
        
        return largestArea
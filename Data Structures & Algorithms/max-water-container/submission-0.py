class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sum=0
        for i in range(len(heights)):
            left=i
            right=len(heights)-1
            while left<right:
                if min(heights[left],heights[right])*(right-left) > sum:
                    sum = min(heights[left],heights[right])*(right-left)
                    right-=1
                right-=1
        return sum
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area=0
        for i in range(len(heights)-1):
            breadth=1
            height=heights[i]
            for j in range(i+1,len(heights)):
                    breadth+=1
                    height=min(heights[j],height)
                    area=max(area,height*breadth)
        for i in range(len(heights)):
            area=max(area, heights[i])
        return area


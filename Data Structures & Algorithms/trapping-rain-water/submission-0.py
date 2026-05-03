class Solution:
    def trap(self, height: List[int]) -> int:
        output=0
        for i in range(len(height)):
            leftmax=rightmax=height[i]
            for j in range(0,i):
                leftmax=max(leftmax,height[j])
            for k in range(i+1,len(height)):
                rightmax=max(rightmax,height[k]) 
            output+= min(leftmax,rightmax) - height[i]
        return output



                
            


            
    

            
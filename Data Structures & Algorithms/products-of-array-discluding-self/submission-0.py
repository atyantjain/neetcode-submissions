class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=1
        leftprod=[]
        for i in nums:
            leftprod.append(left)
            left*=i
            
        right=1
        rightprod=[]
        for i in nums[::-1]:
            rightprod.append(right)
            right*=i
        rightprod=rightprod[::-1]
        final=[]
        for i in range(len(leftprod)):
            final.append(leftprod[i]*rightprod[i])
        return final


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j=len(s)-1
        for i in range(len(s)):
            if j<0 or i>j:
                break
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            j-=1
            
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        output=0
        for i in range(len(s)):
            new=''
            for j in range(i,len(s)):
                if s[j] not in new:
                    new+=s[j]
                    res=len(new)
                else:
                    break
            output=max(output,res)
            
        return output
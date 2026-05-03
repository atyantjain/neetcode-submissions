class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls=[]
        for i in s:
            if i.isalnum()==1:
                ls.append(i.lower())
        if ls==ls[::-1]:
            return True
        return False
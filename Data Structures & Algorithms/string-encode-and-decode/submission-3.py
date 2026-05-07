class Solution:

    def encode(self, strs: List[str]) -> str:
        temp=''
        for word in strs:
            temp=temp+";"+word
        return temp


            

    def decode(self, s: str) -> List[str]:   
        return s.split(";")[1:]

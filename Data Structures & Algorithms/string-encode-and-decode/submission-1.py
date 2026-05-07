class Solution:

    def encode(self, strs: List[str]) -> str:
        temp=''
        for word in strs:
            temp=temp+";"+word
        return temp

            

    def decode(self, s: str) -> List[str]:
        ls=s.split(";")    
        return ls[1:]

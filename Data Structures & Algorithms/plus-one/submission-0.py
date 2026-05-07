class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=0
        n=len(digits)
        j=n-1
        for i in range(n):
            number=number+digits[i]*(10**j)
            j-=1
        number+=1
        ls=[]
        for i in str(number):
            ls.append(int(i))

        return ls
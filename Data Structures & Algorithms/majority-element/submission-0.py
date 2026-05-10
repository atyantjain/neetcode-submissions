class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max=0

        book={}
        for i in nums:
            if i in book:
                book[i]+=1
            else:
                book[i]=1
        for j in book.keys():
            if book[j]>max:
                max=book[j]
                number=j
        return number
                

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        count=0
        longest=0
        nums=list(set(nums))
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                count+=1
                longest=max(count,longest)
            else:
                if count>0:
                    count=0
        return longest+1

        
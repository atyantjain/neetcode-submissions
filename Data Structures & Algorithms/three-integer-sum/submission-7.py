class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ls=[]
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right]==0:
                    ls.append([nums[i],nums[left],nums[right]])
                    right=right-1
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif nums[i]+nums[left]+nums[right]<0:
                    left+=1
                elif nums[i]+nums[left]+nums[right]>0:
                    right-=1

        return ls
    


                          
        
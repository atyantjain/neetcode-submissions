class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if temperatures==[]:
                break
            day=temperatures[0]
            count=0
            for j in temperatures:
                if j>day:
                    output[i]=count
                    break
                else:
                    count+=1
            temperatures.pop(0)
        return output
            

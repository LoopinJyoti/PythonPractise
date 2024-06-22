class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0 
        max=count
        for i in nums: 
            if(i==1):

                count+=1
                print(count)
                if(max<count):
                    max=count
            else: 
                count=0
                print("count reversed to 0")

        return max
            
            
        
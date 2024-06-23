class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        digits=0
        l=0
        for i in nums:
            l=len(str(i))
            if(l%2==0):
                digits+=1
        return digits
            
        
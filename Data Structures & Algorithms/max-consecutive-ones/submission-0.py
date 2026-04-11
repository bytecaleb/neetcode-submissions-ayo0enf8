class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive: int = 0
        count: int = 0

        for n in nums:
            if n == 1:
                count += 1
            else:
                count = 0
            
            if count > max_consecutive:
                max_consecutive = count
        
        return max_consecutive
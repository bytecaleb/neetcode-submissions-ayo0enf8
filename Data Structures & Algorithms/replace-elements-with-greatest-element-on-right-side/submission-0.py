class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_val: int = -1

        for i in range(len(arr) - 1, -1, -1):

            current: int = arr[i]
            arr[i] = max_val

            max_val = max(max_val, current)
        
        return arr
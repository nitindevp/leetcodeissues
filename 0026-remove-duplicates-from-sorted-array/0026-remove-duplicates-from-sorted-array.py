class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        # case - if array is empty
        if not arr:
            return 0 

        i = 0 

        for j in range(1, len(arr)):
            if arr[j] != arr[i]:
                i +=1
                arr[i] = arr[j]
        return i + 1

arr = [1,1,1,2,2,3,3,3,4,5,]
sol = Solution()
k = sol.removeDuplicates(arr)
print(arr[:k])
class Solution():
    def removeDuplicates(self, arr):
        
        # edge case : if array is empty
        if not arr:
            return 0
        # slow pointer 
        i = 0
        
        #fast pointer
        for j in range(1,len(arr)):
            # found a new unique element
            if arr[j] != arr[i]:
                i +=1
                arr[i] = arr[j]
        # number of unique elements 
        return i + 1


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

sol = Solution()
k = sol.removeDuplicates(arr)        
print(arr[:k]) 
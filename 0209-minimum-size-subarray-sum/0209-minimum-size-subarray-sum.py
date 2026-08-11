class Solution:
    def minSubArrayLen(self, target, nums):

        left = 0
        current_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):

            # Expand the window
            current_sum += nums[right]

            
            while current_sum >= target:

                
                window_length = right - left + 1

                
                min_length = min(min_length, window_length)

                
                current_sum -= nums[left]

                
                left += 1

    
        if min_length == float("inf"):
            return 0

        return min_length


nums = [1,2,3,4]
target = 4

sol = Solution()
print(sol.minSubArrayLen(target, nums))
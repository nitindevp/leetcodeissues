class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    
        n = len(nums)

        result = [0] * n

        left = 0
        right = n - 1
        position = n - 1

        while left <= right:

            if abs(nums[left]) > abs(nums[right]):
                result[position] = nums[left] * nums[left]
                left += 1
            else:
                result[position] = nums[right] * nums[right]
                right -= 1

            position -= 1

        return result
nums = [-7, -3, 2, 3, 11]

sol = Solution()
print(sol.sortedSquares(nums))
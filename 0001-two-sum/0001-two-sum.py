class Solution:
    def twoSum(self, nums, target):

        seen = {}

        for i in range(len(nums)):

            needed = target - nums[i]

            if needed in seen:
                return [seen[needed], i]

            seen[nums[i]] = i


# Input
nums = [2, 7, 11, 15]
target = 9

# Create object
sol = Solution()

# Call function
answer = sol.twoSum(nums, target)

# Print answer
print(answer)
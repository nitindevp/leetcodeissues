class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def next_number(num):
            total = 0

            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10

            return total
        slow = n
        fast = n
        while True:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

            if slow == fast:
                break
        return slow == 1


sol = Solution()

print(sol.isHappy(19)) 
print(sol.isHappy(2))  
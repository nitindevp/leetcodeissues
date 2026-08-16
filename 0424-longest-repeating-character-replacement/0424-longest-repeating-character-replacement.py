class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        count = {}
        max_len = 0 
        max_freq = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) + 1

            max_freq = max(max_freq , count[s[right]])

            window_length = right - left + 1
            replacement = window_length - max_freq

            if replacement > k:
                count[s[left]] -= 1
                left += 1

            max_len= max(max_len , right - left + 1)
        return max_len


s = "AABABBA"
k = 1
sol = Solution()
print(sol.characterReplacement(s,k))
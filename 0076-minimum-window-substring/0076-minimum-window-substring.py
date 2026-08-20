class Solution:
    def minWindow(self, s, t):

        
        if not t or not s:
            return ""

        
        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        left = 0
        formed = 0
        required = len(need)

        window = {}

        min_length = float("inf")
        result_start = 0

        
        for right in range(len(s)):

            char = s[right]

            
            window[char] = window.get(char, 0) + 1

            
            if char in need and window[char] == need[char]:
                formed += 1

        
            while formed == required:

                
                window_length = right - left + 1

                
                if window_length < min_length:
                    min_length = window_length
                    result_start = left

                
                left_char = s[left]

                window[left_char] -= 1

                
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

            
                left += 1

        
        if min_length == float("inf"):
            return ""

        return s[result_start: result_start + min_length]


s = "ADOBECODEBANC"
t = "ABC"

sol = Solution()
print(sol.minWindow(s, t))
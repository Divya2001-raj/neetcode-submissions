class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_set = set()
        long_sub=0
        left = 0

        for right in range(len(s)):
            while s[right] in sub_set:
                sub_set.remove(s[left])
                left+=1
            sub_set.add(s[right])

            current_set = right - left + 1
            long_sub=max(long_sub,current_set)
        return long_sub
            

        
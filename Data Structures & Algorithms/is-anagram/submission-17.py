class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts=Counter(s)
        for char in t:
            if char not in counts:
                return False
            counts[char]-=1
            if counts[char]==0:
                del counts[char]
        return len(counts)==0

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    
        if len(s)!=len(t):
            return False
        s_counts=Counter(s)
        for char in t:
            if char not in s_counts:
                return False
            s_counts[char]-=1

            if s_counts[char]==0:
                del s_counts[char]

        return len(s_counts)==0
        
        # if len(s)!=len(t):
        #     return False
        # count={}
        # for char in s:
        #     count[char]=count.get(char,0)+1
        # for char in t:
        #     count[char]=count.get(char,0)-1
        # return all(x==0 for x in count.values())


        # return sorted(s)==sorted(t)
        # return Counter(s)==Counter(t)
        # if len(s)!=len(t):
        #     return False
        
        # count = [0]*26

        # for ch in s:
        #     count[ord(ch)-ord('a')]+=1
        # for ch in t:
        #     count[ord(ch)-ord('a')]-=1

        # for c in count:
        #     if c!=0:
        #         return False
        # return True



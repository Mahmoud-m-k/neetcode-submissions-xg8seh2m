class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        t_ans = {}
        s_ans = {}
        
        for i in range(len(s)):
            t_ans[t[i]] =  t_ans.get(t[i], 0) + 1
            s_ans[s[i]] =  s_ans.get(s[i], 0) + 1

        return t_ans == s_ans   
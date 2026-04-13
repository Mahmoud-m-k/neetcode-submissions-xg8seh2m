class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ''
        for s in strs:
            l = len(s)
            code += str(l)
            code += "#"
            code += s
        return code

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  
            res.append(s[j + 1: j + length + 1])
            i = j + length + 1
        print(res)
        return res
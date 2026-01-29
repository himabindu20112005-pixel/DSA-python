class Solution:
    def partition(self, s):
        res = []
        path = []
        def is_pal(x):
            return x == x[::-1]
        def backtrack(i):
            if i == len(s):
                res.append(path[:])
                return
            for j in range(i, len(s)):
                if is_pal(s[i:j+1]):
                    path.append(s[i:j+1])
                    backtrack(j + 1)
                    path.pop()
        backtrack(0)
        return res

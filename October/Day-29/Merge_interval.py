class Solution:
    def merge(self, intervals):
        intervals.sort()
        
        res = []

        for i in intervals:
            if not res or i[0] > res[-1][1]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])

        return res

class Solution:
    def strStr(self, mainstr,smaller_str):
        for i in range(len(mainstr) - len(smaller_str) + 1):
            for j in range(len(smaller_str)):
                if mainstr[i+j] != smaller_str[j]:
                    break
            else:
                return i
        return -1
Time Complexity: O(n × m)

Optimal:
class Solution:
    def strStr(self, mainstr,smaller_str):
        if smaller_str == "": # If the smaller_str is empty, return 0
            return 0
        n = len(mainstr)
        m = len(smaller_str)
        for i in range(n - m + 1):  # Check every possible starting position
            if mainstr[i:i+m] == smaller_str:    # Compare mainstr with smaller_str
                return i
        return -1

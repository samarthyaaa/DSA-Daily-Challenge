Brute Force:
class Solution(object):
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
Optimal:
def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l < r:
        total = numbers[l] + numbers[r]
        if total == target:
            return [l + 1, r + 1]
        elif total < target:
            l += 1
        else:
            r -= 1

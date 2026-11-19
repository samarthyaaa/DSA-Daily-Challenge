class Solution:
    def nextbigChar(self, letters, target):
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
        return letters[0]
time complexity :O(n)

class Solution:
    def nextGreatestLetter(self, letters, target):
        low = 0
        high = len(letters) - 1
        while low <= high:
            mid = (low + high) // 2
            if letters[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if low == len(letters):
            return letters[0]
        return letters[low]

class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):    # Lengths must be equal
            return False
        temp = s + s     # Join string with itself
        # Check if goal exists in temp
        if goal in temp:
            return True

        return False

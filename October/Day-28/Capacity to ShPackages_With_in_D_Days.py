class Solution(object):
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2

            count = 1
            capacity = 0

            for i in range(len(weights)):
                if capacity + weights[i] <= mid:
                    capacity = capacity + weights[i]
                else:
                    count += 1
                    capacity = weights[i]

            if count <= days:
                high = mid
            else:
                low = mid + 1

        return low

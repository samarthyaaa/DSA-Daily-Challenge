class Solution:
    def totalFruit(self, fruits):
        start = 0
        count = {}
        longest = 0

        for end in range(len(fruits)):
            f = fruits[end]
            count[f] = count.get(f, 0) + 1  # Add fruit

            while len(count) > 2:  # Keep two types
                count[fruits[start]] -= 1  # Decrease count

                if count[fruits[start]] == 0:
                    del count[fruits[start]]  # Remove fruit

                start += 1  # Move start

            size = end - start + 1  # Find length
            if size > longest:
                longest = size  # Update longest

        return longest

class Solution(object):
    def charaRep(self, s, k):
        ans = 0
        for i in range(len(s)):
            count = {}
            maxfreq = 0
            for j in range(i, len(s)):

                ch = s[j]
                if ch not in count:   # Count frequency
                    count[ch] = 0

                count[ch] = count[ch] + 1
              
                if count[ch] > max_freq:  # Find maximum frequency
                    max_freq = count[ch]
                # Calculate window length
                length = j - i + 1
                # Check replacements
                if length - maxfreq <= k:
                    if length > ans:
                        ans = length
                else:
                    break
        return ans

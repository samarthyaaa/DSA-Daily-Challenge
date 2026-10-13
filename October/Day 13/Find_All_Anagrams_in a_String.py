
def findMatch(s, p):
    ans = []
    n = len(s)
    m = len(p)
    for i in range(n - m + 1): # Check each possible window
        a = [0] * 26
        b = [0] * 26
      
        for j in range(m): # Count characters
            for k in range(26):
                if s[i + j] == chr(k + 97):
                    a[k] += 1
                if p[j] == chr(k + 97):
                    b[k] += 1
        if a == b: # Check if both match
            ans.append(i)

    return ans

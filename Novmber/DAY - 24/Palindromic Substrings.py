Brute:
def countstrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if sub == sub[::-1]:
                count += 1
    return count
s = "aaa"
print(countstrings(s))

optimal:
def countSubstrings(s):
    count = 0
    for i in range(len(s)):
        left = i # Odd length palindrome
        right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        left = i # Even length palindrome
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    return count
s = "aaa"
print(countstrings(s))

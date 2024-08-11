s = 'bbcbaba'

res = 0
for c in s:  # Time: O(26)
    l = s.find(c)  # first occurance  # Time: O(N)
    r = s.rfind(c)  # last occurance
    if l > -1:
        res += len(set(s[l + 1:r]))  # count of unique element in middle

print(res)

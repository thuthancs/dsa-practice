def reverse_words(s):
    def helper(l, r):
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    l = 0
    s = list(s)
    n = len(s)

    for r in range(n):
        if s[r] == " ":
            helper(l, r - 1)
            l = (
                r + 1
            )  # the problem is here, should not over-increment l by adding r + 1 to it
        elif r == n - 1:
            helper(l, r)

    return "".join(s)

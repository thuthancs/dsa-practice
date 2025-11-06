def reverse_string(s, k):
    def helper(l, r):
        while l <= r and r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    s = list(s)
    n = len(s)

    for i in range(0, len(s), 2 * k):
        if len(s[i:]) < k:
            helper(i, n - 1)
        else:
            helper(i, i + k - 1)

    return "".join(s)


if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    print(reverse_string(s, k))

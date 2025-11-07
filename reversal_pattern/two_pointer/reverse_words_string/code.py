def reverseWords(s):
    s = s.strip()
    start = 0
    words = []
    for end in range(len(s)):
        if s[end] == " " and s[end + 1] != " ":
            word = s[start:end].strip()
            words.append(word)
            start += end - start
        elif end == len(s) - 1:
            word = s[start : end + 1].strip()
            words.append(word)

    print(words)
    l, r = 0, len(words) - 1
    while l <= r:
        words[l], words[r] = words[r], words[l]
        l += 1
        r -= 1

    return " ".join(words)

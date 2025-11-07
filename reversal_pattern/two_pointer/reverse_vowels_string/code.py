def reverse_vowels(s):
    lower_vowels = ["u", "e", "o", "a", "i"]
    upper_vowels = [v.upper() for v in lower_vowels]
    vowels = lower_vowels + upper_vowels

    s = list(s)
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] in vowels and s[r] in vowels:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        elif s[l] in vowels and s[r] not in vowels:
            r -= 1
        elif s[r] in vowels and s[l] not in vowels:
            l += 1
        else:
            l += 1
            r -= 1

    return "".join(s)

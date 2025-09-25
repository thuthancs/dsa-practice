def reverse_string(s):
    def helper(l, r):
        # base case: when l >= r, stop the recursion
        if l >= r:
            return
        else:
            # swap the positions of two characters
            s[l], s[r] = s[r], s[l]

            # recurse inwards
            helper(l + 1, r - 1)

        l, r = 0, len(s) - 1
        return helper(l, r)

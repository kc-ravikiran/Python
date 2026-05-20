# Write a program in Python to implement Knuth-Morris-Pratt (KMP) string matching algorithm.

# Function to compute LPS (Longest Prefix Suffix) array
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0  # length of previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


# KMP Pattern Searching Function
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    i = 0  # index for text
    j = 0  # index for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

kmp_search(text, pattern)
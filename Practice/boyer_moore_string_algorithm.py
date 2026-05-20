# Write a program in Python to implement Boyer-Moore string matching algorithm.


# Function to create Bad Character Heuristic table
def bad_character_table(pattern):
    bad_char = {}
    m = len(pattern)

    for i in range(m):
        bad_char[pattern[i]] = i  # last occurrence of character

    return bad_char


# Boyer-Moore Search Function
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)

    bad_char = bad_character_table(pattern)

    s = 0  # shift of the pattern

    while s <= n - m:
        j = m - 1

        # Compare from right to left
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # If pattern is found
        if j < 0:
            print(f"Pattern found at index {s}")

            # Shift pattern forward
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            # Shift based on bad character rule
            shift = max(1, j - bad_char.get(text[s + j], -1))
            s += shift


# Example usage
text = "ABAAABCD"
pattern = "ABC"

boyer_moore(text, pattern)
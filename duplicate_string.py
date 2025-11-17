def find_duplicates(s):
    freq = {}
    duplicates = []

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char, count in freq.items():
        if count > 1:
            duplicates.append(char)

    return duplicates


s = "programming"
print("Duplicates:", find_duplicates(s))

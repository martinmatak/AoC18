import string

fname = 'input.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]


def n_of_any_letter(word, n):
    """Return true if any letter repeats in a given word exactly n times"""

    # english alphabet, lowercase (as it is in input file)
    letters = dict.fromkeys(string.ascii_lowercase, 0)

    for letter in word:
        letters[letter] += 1

    for _, value in letters.items():
        if value == n:
            return True

    return False


two_of_any_letter_words = 0
three_of_any_letter_words = 0

for word in content:
    if n_of_any_letter(word, 2):
        two_of_any_letter_words += 1
    if n_of_any_letter(word, 3):
        three_of_any_letter_words +=1

checksum = two_of_any_letter_words * three_of_any_letter_words
print("Checksum is: " + str(checksum))



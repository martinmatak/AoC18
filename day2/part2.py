fname = 'input.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]


def hamdist(str1, str2):
    """Count the # of differences between equal length strings str1 and str2"""

    diffs = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1
    return diffs


similar_words_found = False

# future optimization: no need to iterate through the whole dictionary
for first_word in content:
    for second_word in content:
        if hamdist(first_word, second_word) == 1:
            # find a letter they differ manually :) 
            print("First word : " + first_word)
            print("Second word: " + second_word)
            similar_words_found = True
            break
    if similar_words_found:
        break



filename = "input.txt"


def activate_polymers(stack, delta_range):
    if len(stack) <= 1:
        return
    top_most_character = stack.pop()
    second_top_most_character = stack.pop()
    if ord(top_most_character) + delta_range == ord(second_top_most_character)\
            or ord(top_most_character) - delta_range == ord(second_top_most_character):
        activate_polymers(stack, delta_range)
    else:
        stack.append(second_top_most_character)
        stack.append(top_most_character)


delta_range = ord('a') - ord('A')
min_len = None
for skipping_letter in range(ord('a'), ord('z') + 1):
    stack = []
    with open(filename) as f:
        while True:
            character = f.read(1)
            if not character:
                break
            if character.isalpha():
                if ord(character.lower()) == skipping_letter:
                    continue
                stack.append(character)
                activate_polymers(stack, delta_range)
    print("Polimers left in stack when skipping " + chr(skipping_letter) + " " + str(len(stack)))
    if min_len is None or len(stack) < min_len:
        min_len = len(stack)

print("Minimum length: ", min_len)

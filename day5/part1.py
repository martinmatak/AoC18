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
stack = []
with open(filename) as f:
    while True:
        character = f.read(1)
        if not character:
            print("End of file")
            break
        if character.isalpha():
            stack.append(character)
            activate_polymers(stack, delta_range)

# \n is last read character
print("Polimers left in stack: ", len(stack))
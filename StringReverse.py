def get_string():
    return input("Please enter a string of characters: ")


def reverse_string(sentence):
    chars = [None] * len(sentence)
    index = len(sentence) - 1
    for n in range(len(sentence)):
        chars[index] = sentence[n]
        index -= 1
    return char_to_string(chars)


def char_to_string(chars):
    sentence = ""
    for n in range(len(chars)):
        sentence += chars[n]
    return sentence


def display_result(reversed_sentence):
    print("The reversed sentence:\n" + reversed_sentence)


sentence = get_string()
reversed_sentence = reverse_string(sentence)
display_result(reversed_sentence)
vowels = [['a', 0], ['e', 0], ['i', 0], ['o', 0], ['u', 0]]


def get_sentence():
    return input("Please enter the sentence:")


def count_vowels(sentence):
    vowels_amount = 0
    for n in range(len(sentence)):
        for i in range(len(vowels)):
            if sentence[n] == vowels[i][0]:
                vowels_amount += 1
                vowels_sum(sentence[n])
    return vowels_amount


def vowels_sum(vowel):
    for n in range(len(vowels)):
        if vowels[n][0] == vowels:
            vowels[n][1] += 1


def display_result(vowels_amount):
    print("There are " + str(vowels_amount) + " vowels in the sentence")


sentence = get_sentence()
vowels_amount = count_vowels(sentence)
display_result(vowels_amount)
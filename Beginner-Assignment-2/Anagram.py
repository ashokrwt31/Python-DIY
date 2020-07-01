
def all_words(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for currentElement in all_words(elements[1:]):
            for i in range(len(elements)):
                tmp.append(currentElement[:i] + elements[0:1] + currentElement[i:])
        return tmp


def attempt_check_word(word):
    global counter
    while True:
        if word == anagram_word:
           print("You have guess right word")
           break
        elif word != anagram_word and counter < count:
           print("Please guess again, you have only ", count - counter," attempt left.")
           counter += 1
           attempt_check_word(input("Enter word: "))
        else:
            break

anagram_word = "define"
counter = 1
count = 5

print("Anagram of word",list(all_words(anagram_word)))
print("You have only 5 attempt to guess the right word")
attempt_check_word(input("Enter word: "))



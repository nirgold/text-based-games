def choose_word():
    import json
    import random
    import urllib.request

    url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
    words = json.loads(url.read())
    word = random.choice(words)
    return word


import tkinter as tk





stack = []

word = choose_word()
wl = list(set(word))


def draw(word):
    for char in word:
        if char in stack:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()
    print(sorted(stack))

draw(word)
try_c = 0

while len(wl) > 0:
    letter = input("Your guess please (One letter or whole word)? ")
    trial = letter.lower()
    if len(trial) == 1:
        if trial not in stack:
            stack.append(trial)
            count = 0
            for char in word:
                if trial == char:
                    count += 1
                else:
                    try_c += 1
            print(f"There are {count} {trial} in the word!")
            draw(word)
            if count > 0 and trial in wl:
                wl.remove(trial)
        else:
            print (f"You already tried {trial}")
    else:
        c = 0
        for c in range(len(word)):
            if word[c] == trial[c]:
                c +=1
            else:
                break
        if len(trial) == len(word) and c == len(word):
            wl = []
        else:
            draw(word)


print(f"You won! the word was {word}!")



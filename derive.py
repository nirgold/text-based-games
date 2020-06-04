import enchant
import json
import random
import urllib.request


def choose_word():
    url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
    words = json.loads(url.read())
    word = random.choice(words)
    return word

d = enchant.Dict("en_US")


start_word = choose_word()
while len(start_word) > 4:
    start_word = choose_word()
end_word = choose_word()
while len(end_word) != len(start_word) and start_word != end_word:
    end_word = choose_word()

print(f"Please get from [{start_word}] to [{end_word}]")

while start_word != end_word:
    text = input("The next step is ")
    if d.check(text) and len(text) > 2:
        mid_word = text
    else:
        print("game over")
        break

    count = 0
    char_in = 0
    while char_in < len(start_word):
        if start_word[char_in] != mid_word[char_in]:
            count += 1
        char_in += 1
    if count > 1:
        print("game over")
        break
    else:
        start_word = mid_word

if start_word == end_word:
    print("You won!")
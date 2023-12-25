import random
from pictures import stages

#Ůvod do hry
print("Vítejte ve hře Hangman.\nHádejte nejznámější postavy z filmu American pie")

lives = 6
print(stages[lives])
#generování náhodného slova
words = ["jim", "kevin", "stifler", "finch"]
random_word = random.choice(words)

#generování podtržítek
hidden_word = []
for one_char in random_word:
    hidden_word.append("_")
print(''.join(hidden_word))

while "_" in hidden_word:
    guess = input("Zadejte hádané písmeno: ").lower()
    for index in range(0, len(random_word)):
        if guess == random_word[index]:
            hidden_word[index] = guess

    #kontrola životů
    if guess not in random_word:
        lives -= 1
        print(stages[lives])
    else:
        print(stages[lives])
    print(f"Počet životů: {lives}")
    if lives == 0:
        print("YOU LOOSE")
        break

    print(''.join(hidden_word))

#kontrola vítězství
    if "_" not in hidden_word:
        print("YOU WON!!!!!!!!!!!!!!!!!!!!!!!!!!")
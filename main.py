import csv
import random
import os
import time


def clear_console():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')


def add_voc(voc1, voc2):
    with open('docs/words.csv', 'r', newline='') as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        vocabulary = [line[0].lower() for line in reader]

    if voc1.lower() in vocabulary:
        print("\nWord already exists")
    else:
        with open('docs/words.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voc1, voc2])
            print("\nWord added")

    clear_console()


def learn(r):
    with open('docs/words.csv', 'r', newline='') as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        vocabulary = {line[0]: line[1] for line in reader}

        counter = 0
        for _ in range(0, r):
            random_word = random.choice(list(vocabulary.keys()))

            user_translation = input(f"Translate the word {random_word}: ").strip()

            if user_translation.lower() == vocabulary[random_word].lower():
                print("Correct!")
                counter += 1
            else:
                print(f"Wrong! The correct translation is: {vocabulary[random_word]}")

            clear_console()

        print(f"You got {counter}/{r} words right!")


while True:
    print("""
    1) Add Word
    2) Train
    3) Quit
    """)

    try:
        option = int(input("Choose operation: ").strip())
        if option == 1:
            clear_console()
            word1 = input("Add word in german: ")
            clear_console()
            word2 = input("Add translation in english: ")
            add_voc(word1, word2)
        elif option == 2:
            clear_console()
            rounds = int(input("How many words do you want to learn: "))
            clear_console()
            learn(rounds)
        elif option == 3:
            quit(clear_console())
        else:
            print("Invalid input. Please enter a number.")
            clear_console()
    except ValueError:
        print("Invalid input. Please enter a number.")
        clear_console()

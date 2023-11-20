import random

while True:
    try:
        level = int(input("Level: "))
        num = random.randint(1, level)
        while True:
            try:
                guess = int(input("Guess: "))
                if num == guess:
                    print("Just right!")
                    break
                elif num < guess:
                    print("Too large!")
                else:
                    print("Too small!")
            except ValueError:
                pass
        break
    except ValueError:
        pass

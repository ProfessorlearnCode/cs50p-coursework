import random

def main():
    level = get_level()
    print("--------------------------------")
    print(f"Level: {level}")
    question = generate_integer(level)
    print(f"Your Score: {question}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level == 1 or level == 2 or level == 3:
            return level
        else:
            continue

def generate_integer(level):
    SCORE = 0
    if level == 1:
        for i in range(10):
            TRIES = 0
            x = random.randint(0,9)
            y = random.randint(0,9)
            sum_expression = x + y
            while TRIES < 3:
                try:
                    answer = int(input(f"{x} + {y} = "))
                except ValueError:
                    print("EEE")
                    TRIES += 1
                    continue

                if answer == sum_expression:
                    SCORE += 1
                    break
                elif TRIES == 2:
                    print(f"Correct Answer is {sum_expression}")
                    break
                else:
                    print("EEE")
                    TRIES += 1
                    continue

    elif level == 2 :
        for i in range(10):
            TRIES = 0
            x = random.randint(10,99)
            y = random.randint(10,99)
            sum_expression = x + y
            while TRIES < 3:
                try:
                    answer = int(input(f"{x} + {y} = "))
                except ValueError:
                    print("EEE")
                    TRIES += 1
                    continue

                if answer == sum_expression:
                    SCORE += 1
                    break
                elif TRIES == 2:
                    print(f"Correct Answer is {sum_expression}")
                    break
                else:
                    print("EEE")
                    TRIES += 1
                    continue
    elif level == 3 :
        for i in range(10):
            TRIES = 0
            x = random.randint(100,999)
            y = random.randint(100,999)
            sum_expression = x + y
            while TRIES < 3:
                try:
                    answer = int(input(f"{x} + {y} = "))
                except ValueError:
                    print("EEE")
                    TRIES += 1
                    continue

                if answer == sum_expression:
                    SCORE += 1
                    break
                elif TRIES == 2:
                    print(f"Correct Answer is {sum_expression}")
                    break
                else:
                    print("EEE")
                    TRIES += 1
                    continue
    else:
        pass
    return SCORE

if __name__ == "__main__":
    main()

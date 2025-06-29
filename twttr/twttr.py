
# statement = input("Input: ")

# for vowel in statement:
#     print(vowel.strip("AaEeIiOoUu"), end="")

# print()

def main():
    statement = input("Input: ")
    print(shorten(statement))


def shorten(word):
    expression = ""
    for vowel in word:
        word = vowel.strip("AaEeIiOoUu")
        expression += word
    return expression

if __name__ == "__main__":
    main()
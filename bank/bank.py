
# greeting = input("Greeting: ")
# greeting = greeting.lower().rstrip().lstrip()


# def checkhello():
#     greeting.find("h")
#     greeting.find("hello")
#     if greeting.find("h") == 0:
#         return True
#     else:
#         return False


# if greeting =="hello" or greeting.find("hello") == 0:
#     print("$0")
# elif checkhello():
#     print("$20")
# else:
#     print("$100")


def main():
    greeting = input("greeting: ").strip(" ")
    print(value(greeting))

def value(greeting):
    if greeting.lower() == 'hello':
        return 0
    elif greeting.lower() != 'hello' and greeting.lower().startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()











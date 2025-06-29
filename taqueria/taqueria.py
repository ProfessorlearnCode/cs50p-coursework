

Menu = {
    "bajataco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "superburrito": 8.50,
    "superquesadilla": 9.50,
    "taco": 3.00,
    "tortillasalad": 8.00,
}

# Sum = 0
# while True:
#     user_input = input("Item: ").replace(" ", "")
#     print(user_input)
#     if user_input in Menu:
#         print("Yes")
#     else:
#         print("No")


Sum = 0
while True:
    try:
        user_input = input("Item: ").lower().replace(" ", "")
        if user_input in Menu:
            Sum = Menu[user_input] + Sum
            print(f"Item:${Sum:.2f}")
        else:
            print("The Item not found")
            continue

    except (EOFError,KeyError):
        print()
        break








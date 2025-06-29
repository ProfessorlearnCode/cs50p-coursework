
import inflect

p = inflect.engine()

LIST = []
while True:
    try:
        user_input = input("Name: ")
        LIST.append(user_input)
    except EOFError:
        print()
        break

mylist = p.join((LIST))
print(f"Adieu, adieu, to {mylist}")
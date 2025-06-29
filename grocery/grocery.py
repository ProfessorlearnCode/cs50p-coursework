

grocery_dict = {}

while True:
    try:
        item = input().lower().strip()
        if item in grocery_dict:
            grocery_dict[item] += 1
        else:
            grocery_dict[item] = 1
    except EOFError:
        print("\n")
        for key in sorted(grocery_dict.keys()):
            print(grocery_dict[key], key.upper())
        break
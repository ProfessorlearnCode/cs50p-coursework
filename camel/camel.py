def main():
    name = input("camelCase: ")
    upperfinder(name)

def upperfinder(name):
    for c in name:
        if not c.isupper():
            print(c, end="")
            continue
        else:
            print(c.replace(c,f"_{c.lower()}"), end="")
            continue
    print()

main()



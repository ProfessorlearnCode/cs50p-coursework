
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? " )
answer = answer.lower().rstrip().lstrip()
match answer:
    case "42":
        print("Yes")
    case "forty-two" | "forty two":
        print("Yes")
    # case " forty two" | "forty two " | " 42" | "42 ":
    #     print("No")
    case _:
        print("No")
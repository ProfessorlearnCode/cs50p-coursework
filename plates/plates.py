

def vanityalphabet(plates):
    for alphabet in plates[:1]:
        if alphabet.isalpha() == True:
            return True
        else:
            return False


def vanitylength(plates):
    if len(plates) <= 6 and len(plates) >= 2:
        return True
    else:
        return False


def vanitycharacter(plates):
    if not plates.find('!') == -1 or plates.find('.') != -1 or plates.find(" ") > -1:
        return False
    else:
        return True


def number_ending(plates):
    if plates[-1].isdigit() and plates[-2].isdigit() and plates[-2] != "0":
        return True
    else:
        return False


# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
#     if s.isalpha():
#         if vanityalphabet(s) and vanitylength(s) and vanitycharacter(s):
#             return True
#         else:
#             return False
#     else:
#         if vanityalphabet(s) and vanitylength(s) and vanitycharacter(s) and number_ending(s):
#             return True
#         else:
#             return False


# main()








def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalpha():
        if vanityalphabet(s) and vanitylength(s) and vanitycharacter(s):
            return True
        else:
            return False
    else:
        if vanityalphabet(s) and vanitylength(s) and vanitycharacter(s) and number_ending(s):
            return True
        else:
            return False


if __name__ == "__main__":
    main()
import sys
from tabulate import tabulate


def args_num_checker():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")

    if not sys.argv[1].endswith('csv'):
        sys.exit("Not a CSV file")
    else:
        return sys.argv[1]

def regular_menu():
    REGULAR_MENU_LIST = []
    with open("regular.csv") as csv_regular:
        for row in csv_regular:
            line = row.rstrip().split(",")
            REGULAR_MENU_LIST.append(line)

        return REGULAR_MENU_LIST


def sicilian_menu():
    SICILIAN_MENU_LIST = []
    with open("sicilian.csv") as csv_sicilian:
        for row in csv_sicilian:
            line = row.rstrip().split(",")
            SICILIAN_MENU_LIST.append(line)

        return SICILIAN_MENU_LIST




def main ():
    args_num_checker()

    if args_num_checker() == 'regular.csv':
        print(tabulate(regular_menu(), headers='firstrow', tablefmt="grid"))
    elif args_num_checker() == 'sicilian.csv':
        print(tabulate(sicilian_menu(), headers='firstrow', tablefmt="grid"))
    else:
        sys.exit("File does not exist")


main()




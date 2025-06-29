
import sys

def args_num_checker():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    else:
        return sys.argv

def argument():
    special_list = []
    if not sys.argv[1].endswith('.py'):
        sys.exit("Not a python file")
    try:
        with open(sys.argv[1],'r') as file:
            for line in file.readlines():
                if line.startswith("#"):
                    continue
                elif line.isspace():
                    continue
                elif line.lstrip().startswith('#'):
                    continue
                elif not line.lstrip() == '':
                    line = line.lstrip().rstrip()
                    special_list.append(line)
            return special_list
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    print(len(argument()))
    args_num_checker()

main()

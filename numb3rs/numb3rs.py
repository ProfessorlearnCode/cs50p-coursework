import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        list_of_entries = ip.split(".")
        for check in list_of_entries:
            if int(check) < 0 or int(check) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
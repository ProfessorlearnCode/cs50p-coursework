import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        url_expression = re.search(r"(http(s)*:(\/\/)(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if url_expression:
            url = url_expression.groups()
            return "https://youtu.be/" + url[4]



if __name__ == "__main__":
    main()
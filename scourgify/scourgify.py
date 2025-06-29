import csv
import sys


def reading_csv():
    name_house = []
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for name in reader:
            last, first = name['name'].rstrip().split(", ")
            house = name['house'].rstrip()
            Students = {'first': first,"last":last,"house":house}
            name_house.append(Students)

    return name_house

def writing_csv(list):
    with open(sys.argv[2],"w") as after_csvfile:
        fieldnames=['first','last','house']
        writer = csv.DictWriter(after_csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list)


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    else:
        try:
            data = reading_csv()
            writing_csv(data)
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


main()
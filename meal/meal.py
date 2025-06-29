
def convert(time):
    hr, min = time.split(":")
    conversion = int(hr) + round(int(min)/60, 2)
    return conversion


def main():
    t = input("What Time is it? ")
    timetaken = round(convert(t), 2)
    if 7.00 <= timetaken and 8.00>=timetaken:
        print("Breakfast Time")
    elif 12.00 <= timetaken and 13.00>=timetaken:
        print("Lunch Time")
    elif 18.00 <= timetaken and 19.00>=timetaken:
        print("Dinner Time")
    else:
        print("")

if __name__ == "__main__":
    main()

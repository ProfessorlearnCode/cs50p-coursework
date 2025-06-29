import datetime
import inflect
import re
import sys

p = inflect.engine()
def main():
    date = input("Date of Birth: ")
    try:
        year, month, day = date_check(date)
    except:
        sys.exit("Invalid Date")
    dob = datetime.date(int(year), int(month), int(day))
    today_d = datetime.date.today()
    days_difference = today_d - dob
    minutes = days_difference.days * 24 * 60
    output = p.number_to_words(minutes, andword= '')
    print(output.capitalize() + " minutes")

def date_check(dob):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", dob):
        year, month, day = dob.split('-')
        return (year, month, day)


if __name__ == "__main__":
    main()


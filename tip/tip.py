def main():
    dollars = float(dollars_to_float(input("How much was the meal? ")))
    percent = float(percent_to_float(input("What percentage would you like to tip? ")))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d.removeprefix("$"))
    return (f"{d:.1f}")


def percent_to_float(p):
    # p = input("Enter a percentage :")
    p = float(p.removesuffix("%"))
    p = p/100
    return (f"{p:.2f}"
main()











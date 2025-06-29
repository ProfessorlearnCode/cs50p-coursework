# while True:
#     try:
#         Expression = input("Fraction: ")
#         first, second = Expression.split("/")
#         print(first)
#         print(second)
#         if int(first) > int(second):
#             print("Numerator > Denominator")
#             continue
#         else:
#             print("Numerator < Denominator")
#             break

#     except (ValueError,ZeroDivisionError):
#         print("Error")





# def Calculating_Fractions(f,s):
#     fraction = (int(f) / int(s)) * 100
#     return round(fraction)

# def Decision(e):
#     if e <= 1:
#         return print("E")
#     elif e >= 99:
#         return print("F")
#     else:
#         return print(f"{e}%")

# def main():
#     while True:
#         try:
#             Expression = input("Fraction: ")
#             first, second = Expression.split("/")
#             if int(first) > int(second):
#                 continue
#             else:
#                 Calculating_Fractions(first, second)


#         except (ValueError,ZeroDivisionError):
#             pass
#         else:
#             break

#     expression = Calculating_Fractions(first, second)
#     Decision(expression)


# main()



def main():
    fraction = input("fraction: ")
    fraction_convert = convert(fraction)
    output = gauge(fraction_convert)
    print(output)


def convert(fraction):
    try:
        num, deno = fraction.split("/")
        numerator = int(num)
        denominator = int(deno)
        exp = numerator/denominator
        if exp <= 1:
            return int(exp * 100)
        else:
            fraction = input("Fraction: ")
            pass
    except(ValueError, ZeroDivisionError):
        raise



def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
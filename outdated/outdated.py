

months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]

while True:
    try:
        date = input("Expression: ").lower().strip(" ")
        mm,dd,yyyy = date.split("/")
        mm = int(mm)
        dd = int(dd)
        if mm > 12 or dd > 31:
            continue
        else:
            break

    except (ValueError):
        if date.startswith(('j','f','m','a','s','o','n','d')):
            if '/' in date or ',' not in date:
                continue
            else:
                date1 = date.replace(",","")
                mm,dd,yyyy = date1.split(" ")
                mm = months.index(mm) + 1
                mm = int(mm)
                dd = int(dd)
                if mm > 12 or dd > 31:
                    continue
                else:
                    break

print(f"{(yyyy)}-{(mm):02}-{(dd):02}")


# print(mm)
# print(dd)
# print(yyyy)

# date = input("Expression: ").lower().strip(" ")
# if '/' in date or ',' not in date:
#     print("Yes")
# else:
#     mm, dd, yyyy = date.split(" ")
#     dd = dd.replace(',',"")
#     print(mm)
#     print(dd)
#     print(yyyy)
#     print(f"{yyyy}-{mm:02}-{dd:02}")
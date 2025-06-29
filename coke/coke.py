initial_amount = 50
print("Amount Due:",initial_amount)

while True:
    coin_insert = int(input("Enter Coin: "))
    if coin_insert == 5 or coin_insert == 10 or coin_insert == 25:
        initial_amount = initial_amount - coin_insert
        if initial_amount == 0:
            print("Change Owed:", initial_amount)
            break
        elif initial_amount < 0:
            print("Change Owed:", initial_amount * -1)
            break
        else:
            print("Amount Due:",initial_amount)
    else:
        print("Amount Due:",initial_amount)
        continue






# while True:
#     coin_input = int(input("Enter coin: "))
#     if coin_input == 25 or coin_input == 10 or coin_input == 5:
#         new_amount = initial_amount - coin_input
#         print("Amount Due", new_amount)
#         if new_amount == 0:
#             break

#     else:
#         continue
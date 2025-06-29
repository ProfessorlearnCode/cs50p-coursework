

fruits_Calories = {
    "apple" : "130",
    "avocado" : "50",
    "banana" : "110",
    "cantaloupe" : "50",
    "grapefruit" : "60",
    "grapes" : "90",
    "honeydew Melon" : "50",
    "kiwifruit": "90",
    "strawberry" : "50",
    "sweet cherries" : "100",
    "orange" : "80",
    "watermelon" : "80",
    "pear" : "100"
}

fruit_input = input("Item: ")
fruit = fruit_input.lower()

if fruit in fruits_Calories:
    print("Calories:",fruits_Calories[fruit])
else:
    None

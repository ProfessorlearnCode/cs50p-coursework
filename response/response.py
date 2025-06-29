from validator_collection import validators

email = input("What's your Email address: ")
try:
    validity = validators.email(email)
    print("Valid")
except:
    print("Invalid")

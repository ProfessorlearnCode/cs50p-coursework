
import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Missing Command-line argument")
else:
    try:
        CLI_input = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number ")

    response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    USD_dict = o["bpi"]["USD"]
    float_rate = USD_dict.get("rate_float")
    amount = float(float_rate) * CLI_input
    print(f"${amount:,.4f}")



import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    btc = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response =  requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    price = btc * data["bpi"]["USD"]["rate_float"]
    print(f"${price:,.4f}")
except requests.RequestException:
    sys.exit()

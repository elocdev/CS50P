import requests
import sys
import json

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line arguemnt")
        
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    
    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        output = response.json()
        
        rate_float = output["bpi"]["USD"]["rate_float"]
        per_coin = rate_float * float(sys.argv[1])
        
        print(f"${per_coin:,.4f}")

except requests.RequestException:
    sys.exit()
    

# accept one command line argument for number of bitcoins
# check - try to convert the argument to float, if unsuccessful, quit via sys.exit message
# query the API for bitcoin price index, get the current price from the nested key
# multiply the n by the price and display the output

import sys
import requests

# in case the user inputs two arguments
if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1]) #try to convert n to float
    except:
        print("Command-line argument is not a number")
# in case the user doesnt input the n, second argument
else:
    print("Missing command-line argument")
    sys.exit(1)

# get the info from bitcoin api
try: #just in case the website isnt working
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()
    bitcoin = response["bpi"]["USD"]["rate_float"]
    total = bitcoin * value
    print(f"${total:,.4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)


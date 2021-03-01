import requests

cryptos = ["bitcoin", "ripple", "tron", "cardano"]
response = []
jsonresponse = []
prices = []

for i in range(0, len(cryptos)):
    response.append(requests.get("https://api.alternative.me/v1/ticker/{}/".format(cryptos[i])))
    jsonresponse.append(response[i].json())
    prices.append(round(float(jsonresponse[i][0]["price_usd"]), 2))
    #print(jsonresponse[i][0]["name"] + " - " + str(prices[i]))

    how_much = input("How much {} do you have? ".format(jsonresponse[i][0]["name"]))
    print("You own $ {}".format(round((float(how_much) * prices[i]), 2)))
    print()
    print()

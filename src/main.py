import requests
import json



def makeRequest(url):
    response = requests.get(url)
    return response


def printjson(obj):
    text = json.dumps(obj, sort_keys=True, ident=4)
    print(text)


def main():
    print("Start")

    clientID = ""
    clientSecret = ""

    response = makeRequest("https://nav-deckofcards.herokuapp.com/youwin")
    print("Status code: %i", response.status_code)
    print(response.json())


main()

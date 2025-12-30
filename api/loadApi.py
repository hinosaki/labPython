import requests
import json
import urllib.request


def getKey():
    fileHandlerKey = open("apikey.key", "r")
    return fileHandlerKey.readline()

def get_stock_data():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    response = requests.get(url)

    '''
    200 OK: Request successful, data returned.
    201 Created: New resource created.
    204 No Content: Success but no data returned.
    400 Bad Request: Invalid request.
    401 Unauthorized: Missing or invalid API key.
    500 Internal Server Error: Server encountered an error.
    '''

    if response.status_code == 200:
        data = response.json()
        #print(data)
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        price = data["Time Series (5min)"][last_refreshed]["1. open"]
        return price
    else:
        return None

def fetch_and_print_articles(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        articles = response.json().get('articles', [])

        for index, article in enumerate(articles[:1], start=1):
            print(f"Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n")
    else:
        print(f"Error: {response.status_code}")


def jprint(obj):
    print(json.dumps(obj, sort_keys=True, indent=4))





# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("1"+("*"*40))
    price = get_stock_data()
    symbol = "IBM"
    if price is not None:
        print(f"{symbol}: {price}")
    else:
        print("Failed to retrieve data.")


    print("2"+("*"*40))
    api_endpoint = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=26d1afa7d69a466e9dd81edf17bb2bc8"
    fetch_and_print_articles(api_endpoint)

    API_URL = "https://newsapi.org/v2/top-headlines"
    API_KEY = getKey()

    params = {
        "country": "us",
        "apiKey": API_KEY,
        "pageSize": 1
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")


    print("3"+("*"*40))
    url = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    print(result)

    print("4"+("*"*40))
    url = 'https://dummyjson.com/ip'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

    print(data)
    print(data["userAgent"])

    print("5"+("*"*40))
    url = 'https://dummyjson.com/users/1'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

    # dump the object to a string
    #userJSON = json.dumps(data, indent=4)
    userJSONString = json.dumps(data)
    # othwerwise data is considered as an object and trated as a dictionary
    # using keys to access datas
    print(data["crypto"]['coin'])

    print("6"+("*"*40))

    '''
    {
  "id":2,
  "firstName":"Michael",
  "lastName":"Williams",
  "maidenName":"",
  "age":36,
  "gender":"male",
  "email":"michael.williams@x.dummyjson.com",
  "phone":"+49 258-627-6644",
  "username":"michaelw",
  "password":"michaelwpass",
  "birthDate":"1989-8-10",
  "image":"https://dummyjson.com/icon/michaelw/128",
  "bloodGroup":"B+",
  "height":186.22,
  "weight":76.32,
  "eyeColor":"Red",
  "hair":{
    "color":"Green",
    "type":"Straight"
  },
  "ip":"12.13.116.142",
  "address":{
    "address":"385 Fifth Street",
    "city":"Houston",
    "state":"Alabama",
    "stateCode":"AL",
    "postalCode":"38807",
    "coordinates":{
      "lat":22.815468,
      "lng":115.608581
    },
    "country":"United States"
  },
  "macAddress":"79:15:78:99:60:aa",
  "university":"Ohio State University",
  "bank":{
    "cardExpire":"01/30",
    "cardNumber":"3530633803003665",
    "cardType":"JCB",
    "currency":"USD",
    "iban":"DE26362283149158045865"
  },
  "company":{
    "department":"Support",
    "name":"Spinka - Dickinson",
    "title":"Support Specialist",
    "address":{
      "address":"395 Main Street",
      "city":"Los Angeles",
      "state":"New Hampshire",
      "stateCode":"NH",
      "postalCode":"73442",
      "coordinates":{
        "lat":79.098326,
        "lng":-119.624845
      },
      "country":"United States"
    }
  },
  "ein":"912-602",
  "ssn":"108-953-962",
  "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/97.0.1072.76 Safari/537.36",
  "crypto":{
    "coin":"Bitcoin",
    "wallet":"0xb9fc2fe63b2a6c003f1c324c3bfa53259162181a",
    "network":"Ethereum (ERC20)"
  },
  "role":"admin"
}
    '''

print("6"+("*"*40))
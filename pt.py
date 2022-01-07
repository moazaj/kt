import requests

for _ in range(0,15):

    response = requests.get(url=f"http://api.aladhan.com/v1/calendarByCity?city=dubai&country=United%20arab%20emirates&method={_}&month=01&year=2022")
    print(response.json()["data"][6]["timings"])
import requests
from bs4 import BeautifulSoup

pt = []
pt_mm = []
pt_str = ""

response_pt = requests.get("https://www.khaleejtimes.com/prayer-time-uae")
webpage = response_pt.text

soup = BeautifulSoup(webpage, "html.parser")

links = soup.find_all("p", class_="prayer-time")

for _ in range(6):
    pt.append(links[_].text.strip())
del pt[1]
for p in pt:
    splitted = p.split(":")
    mm = splitted[1]
    pt_mm.append(f":{mm}")

for p in pt:
    splitted = p.split(":")[0]
    pt_str += f"{splitted} "


pt_str += "\n\n"
for p in pt_mm:
    pt_str += f"{p}\n"
print(pt_str)
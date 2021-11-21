import requests
from bs4 import BeautifulSoup

URL = "https://www.retinalscreening.co.uk/patient-information/screening-locations-list/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="slm_results")
loclistEntry = results.find_all("div", class_="loclist-entry")

locationdictionary = {}

for optician in loclistEntry:
    loclistName = optician.find(class_="loclist-name").text
    loclistAddress = optician.find(class_="loclist-address").get_text(separator=" ").strip()
    locationdictionary[loclistName] = loclistAddress

print(locationdictionary)



import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

print("Job Listings\n")

for job in jobs[:10]:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()

    print("Job:", title)
    print("Company:", company)
    print()
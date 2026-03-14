import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("span", class_="titleline")

print("Top Headlines:\n")

for i, title in enumerate(titles[:10], start=1):
    print(i, "-", title.text)
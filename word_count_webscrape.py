from bs4 import BeautifulSoup
import requests

website = input("Enter a website: ")
page = requests.get(f"{website}")
soup = BeautifulSoup(page.content, "html.parser")
body = soup.find("body")

new_body = body.get_text().split()
print(f'There are {len(new_body)} words in the body of the "{website}" website.')
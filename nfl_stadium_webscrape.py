from bs4 import BeautifulSoup
import requests

page = requests.get("https://en.wikipedia.org/wiki/List_of_current_National_Football_League_stadiums")
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find("table").find_next_sibling("table")  # Finds the stadium table on the website
column = table.find_all("th", scope="row")
table2 = table.find_next_sibling("table")  # Finds the next table with the rest of the stadiums
column2 = table2.find_all("th", scope="row")

print(len(column) + len(column2), "NFL Stadiums")
print("-" * 50)
print()
for item in column:
    print(item.get_text())
for item in column2:
    print(item.get_text())
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_technology_companies_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

# Find the second table on the page
table = soup.find_all("table")[1]

# Find all <th> elements in the second table and clean the text
table_titles = [re.sub(r'\[\d+\]', '', title.text).strip() for title in table.find_all("th")]

# Create a DataFrame with the cleaned column titles
data_frame = pd.DataFrame(columns=table_titles)

# Find all rows in the table body
rows = table.find_all("tr")[1:]  # Skip the header row

# Extract the text from each cell in the rows
for row in rows:
    cells = row.find_all(["td", "th"])
    cell_text = [re.sub(r'\[\d+\]', '', cell.text).strip() for cell in cells]
    # Append the data to the DataFrame
    if len(cell_text) == len(table_titles):
        data_frame.loc[len(data_frame)] = cell_text

data_frame.to_csv(r"D:\AllCodes\Python\python_harry\project 1_snake_water_gun_game\SCT_internship\SCT_SD_4\Companies.csv", index = False)

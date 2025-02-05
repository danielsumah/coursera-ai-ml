import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

url = ''
if url == '':
    print('\n\nEnter a URL in the source file\n\n')
    sys.exit()

response = requests.get(url)

if response.status_code == 200:
    print('Request successful!')
else:
    print('Failed to retrieve the webpage')

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.title.text)

# Find the table containing the data
section = soup.find('div', {'class': 'h-dflex h-flex-wrap h-mh--7 h-mb--15'})

rows = section.find_all('div', {'class': 'b-listing-cards__item'})

data = []
for row in rows:
    title = row.find('div', {'class' : 'b-trending-card__title'})
    price = row.find('div', {'class' : 'b-trending-card__price'})

    title = title.text.strip() if title else ''
    price = price.text.strip() if price else ''

    data.append({title, price})

df = pd.DataFrame(data, columns=['Title', 'Price'])

print(df)

# Save the DataFrame to a CSV file
df.to_csv('outdata/scraped_data.csv', index=False)
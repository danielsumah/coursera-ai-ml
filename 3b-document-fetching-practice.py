import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin


base_url = ''
response = requests.get(base_url)
print(response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
else:
    print('Failed to retrieve this webpage')
    exit()

document_link = soup.find('a', {'class': 'btn_form_10k'})['href']
full_url = urljoin(base_url, document_link)
print('Base URL:', base_url)
print('Document LInk:', document_link)
print('Full URL:', full_url)

doc_response = requests.get(full_url)
if response.status_code == 200:
    with open('outdata/financial-reports/tesserent-ltd.pdf', 'wb') as file:
        print('...downloading PDF')
        file.write(doc_response.content)
    print('Document download complete!')
else:
    print('Failed to download document')
    exit()

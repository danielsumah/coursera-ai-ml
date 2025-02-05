import requests
from bs4 import BeautifulSoup
import os

# Step 1: Send an HTTP request to the webpage
url = 'https://example.com/reports'  # Replace with the actual URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
else:
    print('Failed to retrieve the webpage.')
    exit()

# Step 2: Find the document link
document_link = soup.find('a', {'class': 'download-link'})['href']

# Print the document link to verify
print('Document link found:', document_link)


# Handle relative URLs
base_url = 'https://example.com'  # The base URL of the website
full_url = os.path.join(base_url, document_link)
print('Full URL:', full_url)

# Step 3: Download the document
document_response = requests.get(full_url)

# Check if the document request was successful
if document_response.status_code == 200:
    # Save the document to a file
    with open('report.pdf', 'wb') as file:
        file.write(document_response.content)
    print('Document downloaded successfully.')
else:
    print('Failed to download the document. Status code:', document_response.status_code)




# Fetching multiple file---------------------------------------------------------------------------------
# Find all document links on the page
document_links = soup.find_all('a', {'class': 'download-link'})

# Loop through each link and download the corresponding document
for i, link in enumerate(document_links):
    document_url = os.path.join(base_url, link['href'])
    document_response = requests.get(document_url)
    
    if document_response.status_code == 200:
        # Save each document with a unique name
        file_name = f'report_{i+1}.pdf'
        with open(file_name, 'wb') as file:
            file.write(document_response.content)
        print(f'Document {i+1} downloaded successfully as {file_name}.')
    else:
        print(f'Failed to download document {i+1}. Status code:', document_response.status_code)
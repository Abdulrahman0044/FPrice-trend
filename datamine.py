import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape a page with different structures
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    terms = []

    # Scraping from Wikipedia-like pages
    if 'wikipedia' in url:
        content_div = soup.find('div', {'class': 'mw-parser-output'})
        paragraphs = content_div.find_all('p')
        for paragraph in paragraphs:
            text = paragraph.get_text(strip=True)
            if text:  # Save paragraph as a "term" for now
                terms.append((text[:40] + "...", text))  # First 40 chars as the title
            
    return terms

# List of pages to scrape
pages = [
    'https://en.wikipedia.org/wiki/Portal:Agriculture',
    'https://en.wikipedia.org/wiki/Agricultural_economics',
    'https://en.wikipedia.org/wiki/Farm',
    'https://en.wikipedia.org/wiki/Agricultural_soil_science',
    'https://en.wikipedia.org/wiki/Animal_husbandry',
    'https://en.wikipedia.org/wiki/Agricultural_engineering',
    'https://en.wikipedia.org/wiki/Agronomy',
]

# Open CSV for writing the data
with open('farm_terms.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Term'])

    # Loop through all pages
    for page in pages:
        terms = scrape_page(page)
        writer.writerows(terms)

print("All terms have been saved to 'farm_terms.csv'")

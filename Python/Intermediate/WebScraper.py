import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin  

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_html_content(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to fetch the URL: {url}")

def extract_links(url, html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []

    for link in soup.find_all('a', href=True):
        links.append(urljoin(url, link['href']))

    return links

if __name__ == '__main__':
    url = input("Enter the URL to scrape: ")

    try:
        html_content = get_html_content(url)
        extracted_links = extract_links(url, html_content)

        print("Links found:")
        for link in extracted_links:
            print(link)

    except Exception as e:
        print(f"An error occurred: {e}")

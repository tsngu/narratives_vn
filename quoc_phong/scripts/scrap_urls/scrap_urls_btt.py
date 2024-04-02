import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_article_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    urls = set()
    for link in soup.find_all('a', class_='thumb', href=True):
        url = link['href']
        urls.add(url)
    return urls


def write_urls_to_file(urls, filename):
    with open(filename, 'a') as file:
        for url in urls:
            full_url = urljoin("https://baotintuc.vn/", url)
            file.write(full_url + '\n')

def main():
    base_url = "https://baotintuc.vn/Search.aspx?KeySearch=qu%E1%BB%91c%20ph%C3%B2ng"
    max_articles = 500
    num_articles = 0
    urls = set()

    page_number = 1
    while num_articles < max_articles:
        url = base_url if page_number == 1 else f"{base_url}&page={page_number}"
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.content
            article_urls = extract_article_urls(html_content)
            urls.update(article_urls)
            num_articles += len(article_urls)
            write_urls_to_file(article_urls, '../../txt/btt_urls_mc.txt')
            page_number += 1
        else:
            print("Failed to fetch page:", response.status_code)
            break

if __name__ == "__main__":
    main()

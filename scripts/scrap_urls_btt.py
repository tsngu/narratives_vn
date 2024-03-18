import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_article_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    urls = set()
    for link in soup.find_all('a', class_='thumb'):
        url = link.get('href')
        if url:
            urls.add(url)
    return urls

def write_urls_to_file(urls, filename):
    with open(filename, 'a') as file:
        for url in urls:
            full_url = urljoin("https://baotintuc.vn/", url)
            file.write(full_url + '\n')

def main():
    base_url = "https://baotintuc.vn/the-gioi-130ct0"
    max_articles = 500
    num_articles = 0
    collected_urls = set()

    page_number = 1
    while num_articles < max_articles:
        url = base_url if page_number == 1 else f"{base_url}/trang-{page_number}"
        response = requests.get(url + ".htm")
        if response.status_code == 200:
            article_urls = extract_article_urls(response.content)
            new_urls = article_urls - collected_urls
            num_new_urls = len(new_urls)
            if num_new_urls == 0:
                break
            num_articles += num_new_urls
            write_urls_to_file(new_urls, 'article_urls.txt')
            collected_urls.update(new_urls)

            page_number += 1
        else:
            print("Failed to fetch page:", response.status_code)
            break

if __name__ == "__main__":
    main()

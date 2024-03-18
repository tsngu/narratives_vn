import requests
from bs4 import BeautifulSoup

def extract_article_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    urls = set()
    for link in soup.find_all('a', class_='cms-link'):
        url = link.get('href')
        if url:
            urls.add(url)
    return urls

def write_urls_to_file(urls, filename):
    with open(filename, 'a') as file:
        for url in urls:
            file.write(url + '\n')

def main():
    url = "https://www.vietnamplus.vn/thegioi/"
    max_articles = 500
    num_articles = 0

    while num_articles < max_articles:
        response = requests.get(url)
        if response.status_code == 200:
            article_urls = extract_article_urls(response.content)
            num_articles += len(article_urls)
            write_urls_to_file(article_urls, 'article_urls.txt')

            soup = BeautifulSoup(response.content, 'html.parser')  # Mettre à jour le contenu de la soupe
            load_more_button = soup.find('button', class_='more-news control__loadmore')
            if load_more_button:
                url = url  # Nous ne changeons pas l'URL de la page, donc pas besoin de mise à jour ici
            else:
                break
        else:
            print("Failed to fetch page:", response.status_code)
            break

if __name__ == "__main__":
    main()

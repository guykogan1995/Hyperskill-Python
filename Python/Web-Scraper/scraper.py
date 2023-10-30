import os
import string

import requests
from bs4 import BeautifulSoup

url = "https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page=1"
base_url = "https://www.nature.com"
pages = int(input())
type_article = input()
for i in range(pages):
    try:
        os.mkdir("Page_" + str(i+1))
        path = os.getcwd()
        os.chdir(path + "/Page_" + str(i + 1))
    except FileExistsError:
        path = os.getcwd()
        os.chdir(path + "/Page_" + str(i+1))
    if i > 0:
        url = "https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page=" + str(i+1)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    articles = soup.find_all("article")
    final_articles = []
    for article in articles:
        article_type = article.find('span', {'class': 'c-meta__type'}).text
        if type_article == article_type:
            title = article.find("a").text.strip().replace(" ", "_").replace(string.punctuation, "").replace("’", "")\
                .replace("?", "")
            link = base_url + article.find("a", href=True)["href"]
            new_response = requests.get(link)
            new_soup = BeautifulSoup(new_response.content, "html.parser")
            body = ""
            try:
                body = new_soup.find('p', {'class': 'article__teaser'}).text.replace("\n", "")
                final_articles.append(title + ".txt")
            except AttributeError:
                print("WOW! Attribute error")
            article_text = body.replace('\n', '')
            with open(title + ".txt", "wb") as file:
                file.write(body.encode())
    os.chdir("../")
print(final_articles)




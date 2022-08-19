import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser

def searchGoogle(search):
    url = 'https://www.google.com/search?hl=en&q=' + search

    response = requests.get(url)

    with open('output.html', 'wb') as f:
        f.write(response.content)

    scrape(response)
# webbrowser.open('output.html')
def scrape(response):
    soup = BeautifulSoup(response.text, 'lxml')
    find = soup.body.find(class_='BNeawe s3v9rd AP7Wnd')
    # print(find.text)
# BNeawe iBp4i AP7Wnd

# BNeawe s3v9rd AP7Wnd
    facts = soup.body.find_all(class_='BNeawe s3v9rd AP7Wnd')
    i = 0
    for fact in facts:
        i = i+1
        print(fact.text)
        if i == 5:
            break

        # if 'lyrics' in fact.text:
        #     print(fact.text)
    #     if 'Total Carbohydrate ' in fact.text:
    #         print(fact.text)            

    #     if 'Dietary fiber ' in fact.text:
    #         print(fact.text)
    #     if 'Protein ' in fact.text:
    #         print(fact.text)
    #     if 'Total Fat ' in fact.text:   
    #         print(fact.text)

if __name__ == '__main__':
    while True:
        print("\n----------------\n")
        searchGoogle(f'{input("search: ")}')
import urllib
from bs4 import BeautifulSoup
# import requests
# import webbrowser
# # import json
#
# # def log_calories(food_name):
# url = 'https://www.google.com/search?hl=en&q=how tall is eiffel tower'
#
# response = requests.get(url)
#
# with open('output.html', 'wb') as f:
#     f.write(response.content)
#
# webbrowser.open('output.html')
    # scrape(response)

    # j = json.dumps(summary)
    # with open('summary.json', 'w') as f:
    #     f.write(j)
    #     f.close()

# def scrape(response):
#     soup = BeautifulSoup(response.text, 'lxml')
#     kcal = soup.body.find(class_='BNeawe s3v9rd AP7Wnd')
    
#     # summary = json.load(open('summary.json'))

#     # amountMultiplier = amount / 100
#     # summary['kcalories'] += float(kcal.text.split(' ')[0]) * amountMultiplier

#     nutrition_facts = soup.body.find_all(class_='BNeawe s3v9rd AP7Wnd')

#     for fact in nutrition_facts:
#         if 'Total Carbohydrate ' in fact.text:
#             # summary['carbohydrates'] += (float(fact.text.split(' ')[2]) * amountMultiplier)
#             print(fact.text)

#         if 'Dietary fiber ' in fact.text:
#             # summary['fiber'] += (float(fact.text.split(' ')[2]) * amountMultiplier)
#             print(fact.text)
    
#     #     if 'Protein ' in fact.text:
#     #         protein_array = fact.text.split(' ')

#     #         if len(protein_array) == 3:
#     #             # summary['proteins'] += (float(protein_array[1]) * amountMultiplier)
#     #             print(fact.text)

#     #     if 'Total Fat ' in fact.text:
#     #         fat_array = fact.text.split(' ')

#     #         if len(fat_array) == 4:
#     #             summary['fats'] += (float(fat_array[2]) * amountMultiplier)
    
#     # return summary

# if __name__ == '__main__':
#     log_calories('ice cream calories')

from googlesearch import search
import requests

for url in search(ip, stop=10):
            r = requests.get(url)
            title = everything_between(r.text, '<title>', '</title>')
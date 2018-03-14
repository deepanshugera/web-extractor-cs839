
# coding: utf-8

# In[9]:


from lxml import html  
import csv,os,json
import requests
from lxml import etree
from time import sleep


# In[39]:


data_asins= []
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
literature_books_url_1= "https://www.amazon.com/s/ref=sr_pg_"
literature_books_url_2 = "?rh=n%3A283155%2Cn%3A%211000%2Cn%3A17&page="
literature_books_url_3 = "&ie=UTF8&qid=1521012600"
fiction_books_url_1 = "https://www.amazon.com/s/ref=sr_pg_"
fiction_books_url_2 = "?rh=n%3A283155%2Cn%3A%211000%2Cn%3A25&page="
fiction_books_url_3 = "&ie=UTF8&qid=1521018962"
mystery_books_url_1 = "https://www.amazon.com/s/ref=sr_pg_"
mystery_books_url_2 = "?rh=n%3A283155%2Cn%3A%211000%2Cn%3A18&page="
mystery_books_url_3 = "&ie=UTF8&qid=1521019165"


# In[40]:


def getAsinsFromURL(url):
    page = requests.get(url,headers=headers)
    doc= html.fromstring(page.content)
    #print(page.content)
    X_BOOK_ID = '//li[contains(@class,"s-result-item celwidget")]'
    books = doc.xpath(X_BOOK_ID)
    for book in books:
        data_asin = book.get('data-asin')
        data_asins.append(data_asin)
        print(data_asin)
#print(result[0].get('data-asin'))


# In[41]:


def scrapPages():
    for page_no in range(2, 100):
        literature_url = literature_books_url_1 + str(page_no) + literature_books_url_2 +  str(page_no) +literature_books_url_3
        fiction_url = fiction_books_url_1 + str(page_no) + fiction_books_url_2 +  str(page_no) +fiction_books_url_3
        mystery_url = mystery_books_url_1 + str(page_no) + mystery_books_url_2 +  str(page_no) +mystery_books_url_3
        print("LitUrl " + literature_url)
        sleep(3)
        getAsinsFromURL(literature_url)
        print("FicUrl" + fiction_url)
        getAsinsFromURL(fiction_url)
        print("MysUrl" + mystery_url)
        getAsinsFromURL(mystery_url)
    return data_asins
        


# In[ ]:





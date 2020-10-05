import pandas as pd
import numpy as np
import chardet
import requests as re
from bs4 import BeautifulSoup

product_id = pd.read_csv('./data/distinctIds.csv')['id']
product_id.values


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0"
}
base_url = 'https://www.amazon.com/dp/'
urls = []
for item in product_id:
    urls.append(base_url+item)

movie_titles = []
for index in range(5):  # urls.count):
    print("html" + str(index))
    url = urls[index]
    response = re.get(url, headers=headers)
    response = response.text.encode('utf-8', 'ignore').decode('utf-8')
    soup = BeautifulSoup(response, 'lxml')
    spans = soup.find_all(id="productTitle")
    for span in spans:
        title = span.string.replace('\n', '')

        movie_titles.append(title)


a = np.asarray(movie_titles)
titlefile = pd.DataFrame(a,index=None,columns=['title'])
titlefile.to_csv('./data/titles.csv')
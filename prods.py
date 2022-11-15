import requests
import json 
from bs4 import BeautifulSoup
import pandas as pd
baseurl ="https://www.corporategear.com"
prod_urls=[]
categories =[]
cat_imgs=[]
urls = ['https://www.corporategear.com/men-vests.html?v=product-list',
        'https://www.corporategear.com/men-quarter-zips-and-pullovers.html?sort=&v=product-list',
        'https://www.corporategear.com/men-jackets.html?sort=&v=product-list',
        'https://www.corporategear.com/women-vests.html?v=product-list'
        'https://www.corporategear.com/women-jackets.html?v=product-list',
        'https://www.corporategear.com/accessories-bags.html?v=product-list',
        'https://www.corporategear.com/accessories-electronics.html?v=product-list',
        'https://www.corporategear.com/accessories-drinkware.html?v=product-list',
        'https://www.corporategear.com/accessories-office.html?v=product-list',
        'https://www.corporategear.com/accessories-golf-golf-bags.html?v=product-list',
        'https://www.corporategear.com/accessories-golf-golf-balls.html?v=product-list']

ids =['13839','13851','13850','13840','13841','13846','13921','13919','13868','13874']
limit = [{"start":0,"end":180},{"start":180, "end":500}]
for url in urls:
    categories.append(url.split('/')[3])
for cats,url,i in zip(categories,urls,ids):
    session = requests.session()
    r1 = session.get(url)
    cookies= r1.cookies


    headers = {
        'authority': 'www.corporategear.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ur;q=0.8,so;q=0.7,hi;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://www.corporategear.com',
        'referer': url,
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    for li in limit:
        
        data = {
            'newcatid': i,
            'color': '',
            'size': '',
            'type': '',
            'gender': '',
            'price': '',
            'brand': '',
            'sortby': '',
            'url': cats,
            'startrow': li.get('start'),
            'endrow': li.get('end'),
        }

        response = session.post('https://www.corporategear.com/Category/Getpaggingdata', cookies=cookies, headers=headers, data=data)

        data= response.json()
        data= json.dumps(data)
        data= json.loads(data)
        soup = BeautifulSoup(data['strGrid'],'lxml')
        prods=soup.findAll('a', title=True)
        cat_img= soup.findAll('figure',class_='pro1')
        for p in prods:
            prod_urls.append(baseurl+p.get('href'))
            # cat_imgs.append(img.get('data-images'))
            print(baseurl+p.get('href'))

print(len(prod_urls))
print(len(cat_imgs))
data_dict = {"Product URL":prod_urls}
df= pd.DataFrame.from_dict(data_dict)
df.to_csv("prods-1.csv",index=False)
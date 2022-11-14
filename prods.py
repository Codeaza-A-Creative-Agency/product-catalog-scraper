import requests
import json 
from bs4 import BeautifulSoup
from pprint import pprint
baseurl ="https://www.corporategear.com"
urls = ['https://www.corporategear.com/men-vests.html?v=product-list', 'https://www.corporategear.com/men-quarter-zips-and-pullovers.html?sort=&v=product-list','https://www.corporategear.com/men-jackets.html?sort=&v=product-list','https://www.corporategear.com/women-vests.html?v=product-list'
       'https://www.corporategear.com/women-jackets.html?v=product-list','https://www.corporategear.com/accessories-bags.html?v=product-list','https://www.corporategear.com/accessories-electronics.html?v=product-list','https://www.corporategear.com/accessories-drinkware.html?v=product-list','https://www.corporategear.com/accessories-office.html?v=product-list','https://www.corporategear.com/accessories-golf-golf-bags.html?v=product-list','https://www.corporategear.com/accessories-golf-golf-balls.html?v=product-list']
categories =[]
for url in urls:
    print(url.split('/')[3])
    categories.append(url.split('/')[3])
prod_url=[]
cat_imgs=[]
for cats,url in zip(categories,urls):
    imgs =[]
    cookies = {
        'ASP.NET_SessionId': 'gggaum2fiuxeejptjabbz1cv',
        'VisiterID': '986a0d87-4032-4983-87a2-a8663ed2bc17',
        '_gcl_au': '1.1.975566304.1668408536',
        '_gid': 'GA1.2.1199791776.1668408537',
        'ln_or': 'd',
        '_fbp': 'fb.1.1668408537270.1196558888',
        '__insp_wid': '1939799058',
        '__insp_nv': 'true',
        '__insp_targlpu': 'aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vbWVuLXZlc3RzLmh0bWw%2Fdj1wcm9kdWN0LWxpc3Q%3D',
        '__insp_targlpt': 'Q3VzdG9tIFZlc3RzICYgTDNEpUTHQoQUJMHLrErGJyHg89uy71MyuHRlcmVkIHdpdGggWW91ciBDb3Jwb3JhdGUgTG9nbw%3D%3D',
        '__insp_norec_sess': 'true',
        '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDExMDIwLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5jb3Jwb3JhdGVnZWFyLmNvbS9tZW4tdmVzdHMuaHRtbD92PXByb2R1Y3QtbGlzdCJ9fQ==',
        '_uetsid': '6991c4c063e811ed918e1d3d3c1a5aeb',
        '_uetvid': '6992a9f063e811ed9bb2db5b89275a12',
        '_ga': 'GA1.2.2070327007.1668408537',
        '_dc_gtm_UA-159937545-2': '1',
        '_ga_P2P1R3FERZ': 'GS1.1.1668408536.1.1.1668411021.0.0.0',
        '__insp_slim': '1668411021915',
    }

    headers = {
        'authority': 'www.corporategear.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ur;q=0.8,so;q=0.7,hi;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'ASP.NET_SessionId=gggaum2fiuxeejptjabbz1cv; VisiterID=986a0d87-4032-4983-87a2-a8663ed2bc17; _gcl_au=1.1.975566304.1668408536; _gid=GA1.2.1199791776.1668408537; ln_or=d; _fbp=fb.1.1668408537270.1196558888; __insp_wid=1939799058; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vbWVuLXZlc3RzLmh0bWw%2Fdj1wcm9kdWN0LWxpc3Q%3D; __insp_targlpt=Q3VzdG9tIFZlc3RzICYgTDNEpUTHQoQUJMHLrErGJyHg89uy71MyuHRlcmVkIHdpdGggWW91ciBDb3Jwb3JhdGUgTG9nbw%3D%3D; __insp_norec_sess=true; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDExMDIwLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5jb3Jwb3JhdGVnZWFyLmNvbS9tZW4tdmVzdHMuaHRtbD92PXByb2R1Y3QtbGlzdCJ9fQ==; _uetsid=6991c4c063e811ed918e1d3d3c1a5aeb; _uetvid=6992a9f063e811ed9bb2db5b89275a12; _ga=GA1.2.2070327007.1668408537; _dc_gtm_UA-159937545-2=1; _ga_P2P1R3FERZ=GS1.1.1668408536.1.1.1668411021.0.0.0; __insp_slim=1668411021915',
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

    data = {
        'newcatid': '13839',
        'color': '',
        'size': '',
        'type': '',
        'gender': '',
        'price': '',
        'brand': '',
        'sortby': '',
        'url': cats,
        'startrow': '1',
        'endrow': '3000',
        'guidnew': '31beb67a-f76a-42a1-9d29-f8c6fa0e63d7',
    }

    response = requests.post('https://www.corporategear.com/Category/Getpaggingdata', cookies=cookies, headers=headers, data=data)
    data= response.json()
    data= json.dumps(data)
    data= json.loads(data)
    print(response.url)
    soup = BeautifulSoup(data['strGrid'],'lxml')
    prods=soup.findAll('a', title=True)
    cat_img= soup.findAll('figure',class_='pro1')
    for p,img in zip(prods,cat_img):
        prod_url.append(baseurl+p.get('href'))
        cat_imgs.append(img.get('data-images'))
print(len(prods))
print(len(cat_imgs))
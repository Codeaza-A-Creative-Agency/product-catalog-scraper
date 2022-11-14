#!/usr/bin/env python
# coding: utf-8

# In[1]:




import requests

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
    'referer': 'https://www.corporategear.com/men-vests.html?v=product-list',
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
    'url': '/men-vests.html',
    'startrow': '1',
    'endrow': '95',
    'guidnew': '31beb67a-f76a-42a1-9d29-f8c6fa0e63d7',
}

response = requests.post('https://www.corporategear.com/Category/Getpaggingdata', cookies=cookies, headers=headers, data=data)


# In[329]:


response.text


# In[330]:


data= response.json()


# In[333]:


import json 
from bs4 import BeautifulSoup
from pprint import pprint
data= json.dumps(data)
data= json.loads(data)
baseurl ="https://www.corporategear.com"

soup = BeautifulSoup(data['strGrid'],'lxml')
# print(soup.prettify())

prods=soup.findAll('a', title=True)
cat_img= soup.findAll('figure',class_='pro1')
prod_urls= []
cat_imgs=[]
for urls,img in zip(prods,cat_img):

    imgs =img.get('data-images')
    prod_urls.append(baseurl+urls.get('href'))
    cat_imgs.append(imgs)


# In[334]:


print(len(prod_urls))
print(len(cat_imgs))


# In[ ]:


get_ipython().set_next_input('men-quarter-zips-and-pullovers.html');get_ipython().run_line_magic('pinfo', 'pullovers.html')


# In[340]:


import requests

cookies = {
    'ASP.NET_SessionId': 'gggaum2fiuxeejptjabbz1cv',
    'VisiterID': '986a0d87-4032-4983-87a2-a8663ed2bc17',
    '_gcl_au': '1.1.975566304.1668408536',
    '_gid': 'GA1.2.1199791776.1668408537',
    'ln_or': 'd',
    '_fbp': 'fb.1.1668408537270.1196558888',
    '__insp_wid': '1939799058',
    '__insp_nv': 'true',
    '__insp_targlpu': 'aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D',
    '__insp_targlpt': 'U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0',
    '__insp_norec_sess': 'true',
    '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDIwODk5LCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=',
    '__insp_slim': '1668420900525',
    '_uetsid': '6991c4c063e811ed918e1d3d3c1a5aeb',
    '_uetvid': '6992a9f063e811ed9bb2db5b89275a12',
    '_ga': 'GA1.2.2070327007.1668408537',
    '_ga_P2P1R3FERZ': 'GS1.1.1668408536.1.1.1668420901.0.0.0',
}

headers = {
    'authority': 'www.corporategear.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ur;q=0.8,so;q=0.7,hi;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ASP.NET_SessionId=gggaum2fiuxeejptjabbz1cv; VisiterID=986a0d87-4032-4983-87a2-a8663ed2bc17; _gcl_au=1.1.975566304.1668408536; _gid=GA1.2.1199791776.1668408537; ln_or=d; _fbp=fb.1.1668408537270.1196558888; __insp_wid=1939799058; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D; __insp_targlpt=U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0; __insp_norec_sess=true; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDIwODk5LCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=; __insp_slim=1668420900525; _uetsid=6991c4c063e811ed918e1d3d3c1a5aeb; _uetvid=6992a9f063e811ed9bb2db5b89275a12; _ga=GA1.2.2070327007.1668408537; _ga_P2P1R3FERZ=GS1.1.1668408536.1.1.1668420901.0.0.0',
    'dnt': '1',
    'origin': 'https://www.corporategear.com',
    'referer': 'https://www.corporategear.com/men-quarter-zips-and-pullovers.html?sort=&v=product-list',
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
    'newcatid': '13851',
    'color': '',
    'size': '',
    'type': '',
    'gender': '',
    'price': '',
    'brand': '',
    'sortby': '',
    'url': '/men-quarter-zips-and-pullovers.html?',
    'startrow': '180',
    'endrow': '213',
    #213
    'guidnew': '9f9e4543-3a9d-4b2c-884e-fb2566c719a2',
}

response = requests.post('https://www.corporategear.com/Category/Getpaggingdata', cookies=cookies, headers=headers, data=data)


# In[341]:


response.text


# In[120]:





# In[ ]:





# In[ ]:





# In[121]:





# In[342]:


data= response.json()


# In[343]:


import json 
from bs4 import BeautifulSoup
from pprint import pprint
data= response.json()
data= json.dumps(data)
data= json.loads(data)
# print(data['strGrid'])
baseurl ="https://www.corporategear.com"
soup = BeautifulSoup(data['strGrid'],'lxml')


# In[170]:


print(soup.prettify())


# In[ ]:





# In[344]:


prods=soup.findAll('a', title=True)
cat_img= soup.findAll('figure',class_='pro1')
# prod_urls= []

# cat_imgs=[]
print(len(prods))
print(len(cat_img))
for urls,img in zip(prods,cat_img):

    imgs =img.get('data-images')


    prod_urls.append(baseurl+urls.get('href'))
    cat_imgs.append(imgs)


# In[345]:


print(len(prod_urls))
print(len(cat_imgs))


# In[346]:


import requests

cookies = {
    'ASP.NET_SessionId': 'gggaum2fiuxeejptjabbz1cv',
    'VisiterID': '986a0d87-4032-4983-87a2-a8663ed2bc17',
    '_gcl_au': '1.1.975566304.1668408536',
    '_gid': 'GA1.2.1199791776.1668408537',
    'ln_or': 'd',
    '_fbp': 'fb.1.1668408537270.1196558888',
    '__insp_wid': '1939799058',
    '__insp_nv': 'true',
    '__insp_targlpu': 'aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D',
    '__insp_targlpt': 'U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0',
    '__insp_norec_sess': 'true',
    '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDIzNDM0LCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=',
    '_ga': 'GA1.2.2070327007.1668408537',
    '_uetsid': '6991c4c063e811ed918e1d3d3c1a5aeb',
    '_uetvid': '6992a9f063e811ed9bb2db5b89275a12',
    '__insp_slim': '1668423435868',
    '_ga_P2P1R3FERZ': 'GS1.1.1668408536.1.1.1668423446.0.0.0',
}

headers = {
    'authority': 'www.corporategear.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ur;q=0.8,so;q=0.7,hi;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ASP.NET_SessionId=gggaum2fiuxeejptjabbz1cv; VisiterID=986a0d87-4032-4983-87a2-a8663ed2bc17; _gcl_au=1.1.975566304.1668408536; _gid=GA1.2.1199791776.1668408537; ln_or=d; _fbp=fb.1.1668408537270.1196558888; __insp_wid=1939799058; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D; __insp_targlpt=U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0; __insp_norec_sess=true; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDIzNDM0LCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=; _ga=GA1.2.2070327007.1668408537; _uetsid=6991c4c063e811ed918e1d3d3c1a5aeb; _uetvid=6992a9f063e811ed9bb2db5b89275a12; __insp_slim=1668423435868; _ga_P2P1R3FERZ=GS1.1.1668408536.1.1.1668423446.0.0.0',
    'dnt': '1',
    'origin': 'https://www.corporategear.com',
    'referer': 'https://www.corporategear.com/men-jackets.html?sort=&v=product-list',
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
    'newcatid': '13850',
    'color': '',
    'size': '',
    'type': '',
    'gender': '',
    'price': '',
    'brand': '',
    'sortby': '',
    'url': '/men-jackets.html',
    'startrow': '1',
    'endrow': '208',
    #208
    'guidnew': '5f839c0f-3c40-4fa3-86e7-ff9c2d693789',
}

response = requests.post('https://www.corporategear.com/Category/Getpaggingdata', cookies=cookies, headers=headers, data=data)


# In[347]:


response.text


# In[348]:


import json 
from bs4 import BeautifulSoup
from pprint import pprint
data= response.json()
data= json.dumps(data)
data= json.loads(data)
# print(data['strGrid'])
baseurl ="https://www.corporategear.com"
soup = BeautifulSoup(data['strGrid'],'lxml')


# In[349]:


prods=soup.findAll('a', title=True)
cat_img= soup.findAll('figure',class_='pro1')
# prod_urls= []
us =[]
c_img=[]
# cat_imgs=[]
print(len(prods))
print(len(cat_img))
for urls,img in zip(prods,cat_img):

    imgs =img.get('data-images')


    prod_urls.append(baseurl+urls.get('href'))
    cat_imgs.append(imgs)


# In[350]:


print(len(prod_urls))
print(len(cat_imgs))


# In[351]:


import requests

cookies = {
    'ASP.NET_SessionId': 'gggaum2fiuxeejptjabbz1cv',
    'VisiterID': '986a0d87-4032-4983-87a2-a8663ed2bc17',
    '_gcl_au': '1.1.975566304.1668408536',
    '_gid': 'GA1.2.1199791776.1668408537',
    'ln_or': 'd',
    '_fbp': 'fb.1.1668408537270.1196558888',
    '__insp_wid': '1939799058',
    '__insp_nv': 'true',
    '__insp_targlpu': 'aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D',
    '__insp_targlpt': 'U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0',
    '__insp_norec_sess': 'true',
    '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDI0MzI2LCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=',
    '_uetsid': '6991c4c063e811ed918e1d3d3c1a5aeb',
    '_uetvid': '6992a9f063e811ed9bb2db5b89275a12',
    '_dc_gtm_UA-159937545-2': '1',
    '_ga': 'GA1.2.2070327007.1668408537',
    '__insp_slim': '1668424328692',
    '_ga_P2P1R3FERZ': 'GS1.1.1668408536.1.1.1668424329.0.0.0',
}

headers = {
    'authority': 'www.corporategear.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ur;q=0.8,so;q=0.7,hi;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ASP.NET_SessionId=gggaum2fiuxeejptjabbz1cv; VisiterID=986a0d87-4032-4983-87a2-a8663ed2bc17; _gcl_au=1.1.975566304.1668408536; _gid=GA1.2.1199791776.1668408537; ln_or=d; _fbp=fb.1.1668408537270.1196558888; __insp_wid=1939799058; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D; __insp_targlpt=U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0; __insp_norec_sess=true; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDI0MzI2LCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=; _uetsid=6991c4c063e811ed918e1d3d3c1a5aeb; _uetvid=6992a9f063e811ed9bb2db5b89275a12; _dc_gtm_UA-159937545-2=1; _ga=GA1.2.2070327007.1668408537; __insp_slim=1668424328692; _ga_P2P1R3FERZ=GS1.1.1668408536.1.1.1668424329.0.0.0',
    'dnt': '1',
    'origin': 'https://www.corporategear.com',
    'referer': 'https://www.corporategear.com/women-vests.html?v=product-list',
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
    'newcatid': '13840',
    'color': '',
    'size': '',
    'type': '',
    'gender': '',
    'price': '',
    'brand': '',
    'sortby': '',
    'url': '/women-vests.html',
    'startrow': '1',
    'endrow': '45',
    'guidnew': '81ed77bb-ac01-4e7d-be67-ea1419a608bd',
}

response = requests.post('https://www.corporategear.com/Category/Getpaggingdata', cookies=cookies, headers=headers, data=data)


# In[352]:


response.text


# In[353]:


import json 
from bs4 import BeautifulSoup
from pprint import pprint
data= response.json()
data= json.dumps(data)
data= json.loads(data)
# print(data['strGrid'])
baseurl ="https://www.corporategear.com"
soup = BeautifulSoup(data['strGrid'],'lxml')


# In[354]:


prods=soup.findAll('a', title=True)
cat_img= soup.findAll('figure',class_='pro1')
# prod_urls= []
gen= []
# cat_imgs=[]
print(len(prods))
print(len(cat_img))
for urls,img in zip(prods,cat_img):

    imgs =img.get('data-images')


    prod_urls.append(baseurl+urls.get('href'))
    cat_imgs.append(imgs)
    gen.append("Women")


# In[326]:





# In[355]:


print(len(prod_urls))
print(len(cat_imgs))
print(len(gen))


# In[356]:


import requests

cookies = {
    'ASP.NET_SessionId': 'gggaum2fiuxeejptjabbz1cv',
    'VisiterID': '986a0d87-4032-4983-87a2-a8663ed2bc17',
    '_gcl_au': '1.1.975566304.1668408536',
    '_gid': 'GA1.2.1199791776.1668408537',
    'ln_or': 'd',
    '_fbp': 'fb.1.1668408537270.1196558888',
    '__insp_wid': '1939799058',
    '__insp_nv': 'true',
    '__insp_targlpu': 'aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D',
    '__insp_targlpt': 'U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0',
    '__insp_norec_sess': 'true',
    '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDI0NDk4LCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=',
    '_uetsid': '6991c4c063e811ed918e1d3d3c1a5aeb',
    '_uetvid': '6992a9f063e811ed9bb2db5b89275a12',
    '_dc_gtm_UA-159937545-2': '1',
    '_ga': 'GA1.2.2070327007.1668408537',
    '__insp_slim': '1668424502171',
    '_ga_P2P1R3FERZ': 'GS1.1.1668408536.1.1.1668424518.0.0.0',
}

headers = {
    'authority': 'www.corporategear.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ur;q=0.8,so;q=0.7,hi;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ASP.NET_SessionId=gggaum2fiuxeejptjabbz1cv; VisiterID=986a0d87-4032-4983-87a2-a8663ed2bc17; _gcl_au=1.1.975566304.1668408536; _gid=GA1.2.1199791776.1668408537; ln_or=d; _fbp=fb.1.1668408537270.1196558888; __insp_wid=1939799058; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D; __insp_targlpt=U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0; __insp_norec_sess=true; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDI0NDk4LCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=; _uetsid=6991c4c063e811ed918e1d3d3c1a5aeb; _uetvid=6992a9f063e811ed9bb2db5b89275a12; _dc_gtm_UA-159937545-2=1; _ga=GA1.2.2070327007.1668408537; __insp_slim=1668424502171; _ga_P2P1R3FERZ=GS1.1.1668408536.1.1.1668424518.0.0.0',
    'dnt': '1',
    'origin': 'https://www.corporategear.com',
    'referer': 'https://www.corporategear.com/women-jackets.html?v=product-list',
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
    'newcatid': '13841',
    'color': '',
    'size': '',
    'type': '',
    'gender': '',
    'price': '',
    'brand': '',
    'sortby': '',
    'url': '/women-jackets.html',
    'startrow': '1',
    'endrow': '180',
    'guidnew': '7bba2c89-6b7f-4b7e-a26a-7dc51e83a7d8',
}

response = requests.post('https://www.corporategear.com/Category/Getpaggingdata', cookies=cookies, headers=headers, data=data)


# In[357]:


response.text


# In[358]:


import json 
from bs4 import BeautifulSoup
from pprint import pprint
data= response.json()
data= json.dumps(data)
data= json.loads(data)
# print(data['strGrid'])
baseurl ="https://www.corporategear.com"
soup = BeautifulSoup(data['strGrid'],'lxml')


# In[359]:


prods=soup.findAll('a', title=True)
cat_img= soup.findAll('figure',class_='pro1')
# prod_urls= []
# gen =[
# cat_imgs=[]
print(len(prods))
print(len(cat_img))
for urls,img in zip(prods,cat_img):

    imgs =img.get('data-images')


    prod_urls.append(baseurl+urls.get('href'))
    cat_imgs.append(imgs)
    gen.append('Women')


# In[360]:


print(len(gen))


# In[361]:


import requests

cookies = {
    'ASP.NET_SessionId': 'gggaum2fiuxeejptjabbz1cv',
    'VisiterID': '986a0d87-4032-4983-87a2-a8663ed2bc17',
    '_gcl_au': '1.1.975566304.1668408536',
    '_gid': 'GA1.2.1199791776.1668408537',
    'ln_or': 'd',
    '_fbp': 'fb.1.1668408537270.1196558888',
    '__insp_wid': '1939799058',
    '__insp_nv': 'true',
    '__insp_targlpu': 'aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D',
    '__insp_targlpt': 'U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0',
    '__insp_norec_sess': 'true',
    '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDI0ODg2LCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=',
    '_uetsid': '6991c4c063e811ed918e1d3d3c1a5aeb',
    '_uetvid': '6992a9f063e811ed9bb2db5b89275a12',
    '_ga': 'GA1.2.2070327007.1668408537',
    '__insp_slim': '1668424889461',
    '_ga_P2P1R3FERZ': 'GS1.1.1668408536.1.1.1668424893.0.0.0',
}

headers = {
    'authority': 'www.corporategear.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ur;q=0.8,so;q=0.7,hi;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ASP.NET_SessionId=gggaum2fiuxeejptjabbz1cv; VisiterID=986a0d87-4032-4983-87a2-a8663ed2bc17; _gcl_au=1.1.975566304.1668408536; _gid=GA1.2.1199791776.1668408537; ln_or=d; _fbp=fb.1.1668408537270.1196558888; __insp_wid=1939799058; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D; __insp_targlpt=U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0; __insp_norec_sess=true; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDI0ODg2LCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=; _uetsid=6991c4c063e811ed918e1d3d3c1a5aeb; _uetvid=6992a9f063e811ed9bb2db5b89275a12; _ga=GA1.2.2070327007.1668408537; __insp_slim=1668424889461; _ga_P2P1R3FERZ=GS1.1.1668408536.1.1.1668424893.0.0.0',
    'dnt': '1',
    'origin': 'https://www.corporategear.com',
    'referer': 'https://www.corporategear.com/accessories-bags.html?v=product-list',
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
    'newcatid': '13846',
    'color': '',
    'size': '',
    'type': '',
    'gender': '',
    'price': '',
    'brand': '',
    'sortby': '',
    'url': '/accessories-bags.html',
    'startrow': '1',
    'endrow': '180',
    'guidnew': '850544b7-8d4b-4311-ba72-b86a2fad2c27',
}

response = requests.post('https://www.corporategear.com/Category/Getpaggingdata', cookies=cookies, headers=headers, data=data)


# In[362]:


response.text


# In[363]:


import json 
from bs4 import BeautifulSoup
from pprint import pprint
data= response.json()
data= json.dumps(data)
data= json.loads(data)
# print(data['strGrid'])
baseurl ="https://www.corporategear.com"
soup = BeautifulSoup(data['strGrid'],'lxml')


# In[364]:


prods=soup.findAll('a', title=True)
cat_img= soup.findAll('figure',class_='pro1')
# prod_urls= []

# cat_imgs=[]
print(len(prods))
print(len(cat_img))
for urls,img in zip(prods,cat_img):

    imgs =img.get('data-images')


    prod_urls.append(baseurl+urls.get('href'))
    cat_imgs.append(imgs)


# In[365]:


print(len(prod_urls))
print(len(cat_imgs))
print(len(gen))


# In[366]:


import requests

cookies = {
    'ASP.NET_SessionId': 'gggaum2fiuxeejptjabbz1cv',
    'VisiterID': '986a0d87-4032-4983-87a2-a8663ed2bc17',
    '_gcl_au': '1.1.975566304.1668408536',
    '_gid': 'GA1.2.1199791776.1668408537',
    'ln_or': 'd',
    '_fbp': 'fb.1.1668408537270.1196558888',
    '__insp_wid': '1939799058',
    '__insp_nv': 'true',
    '__insp_targlpu': 'aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D',
    '__insp_targlpt': 'U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0',
    '__insp_norec_sess': 'true',
    '_dc_gtm_UA-159937545-2': '1',
    '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDI1NDgxLCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=',
    '_uetsid': '6991c4c063e811ed918e1d3d3c1a5aeb',
    '_uetvid': '6992a9f063e811ed9bb2db5b89275a12',
    '_ga': 'GA1.2.2070327007.1668408537',
    '__insp_slim': '1668425483167',
    '_ga_P2P1R3FERZ': 'GS1.1.1668408536.1.1.1668425484.0.0.0',
}

headers = {
    'authority': 'www.corporategear.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ur;q=0.8,so;q=0.7,hi;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ASP.NET_SessionId=gggaum2fiuxeejptjabbz1cv; VisiterID=986a0d87-4032-4983-87a2-a8663ed2bc17; _gcl_au=1.1.975566304.1668408536; _gid=GA1.2.1199791776.1668408537; ln_or=d; _fbp=fb.1.1668408537270.1196558888; __insp_wid=1939799058; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D; __insp_targlpt=U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0; __insp_norec_sess=true; _dc_gtm_UA-159937545-2=1; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDI1NDgxLCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=; _uetsid=6991c4c063e811ed918e1d3d3c1a5aeb; _uetvid=6992a9f063e811ed9bb2db5b89275a12; _ga=GA1.2.2070327007.1668408537; __insp_slim=1668425483167; _ga_P2P1R3FERZ=GS1.1.1668408536.1.1.1668425484.0.0.0',
    'dnt': '1',
    'origin': 'https://www.corporategear.com',
    'referer': 'https://www.corporategear.com/accessories-electronics.html?v=product-list',
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
    'newcatid': '13921',
    'color': '',
    'size': '',
    'type': '',
    'gender': '',
    'price': '',
    'brand': '',
    'sortby': '',
    'url': '/accessories-electronics.html',
    'startrow': '1',
    'endrow': '27',
    'guidnew': '03ad7fdb-85aa-4c6d-8c58-645d5922d77b',
}

response = requests.post('https://www.corporategear.com/Category/Getpaggingdata', cookies=cookies, headers=headers, data=data)


# In[367]:


response.text


# In[368]:


import json 
from bs4 import BeautifulSoup
from pprint import pprint
data= response.json()
data= json.dumps(data)
data= json.loads(data)
# print(data['strGrid'])
baseurl ="https://www.corporategear.com"
soup = BeautifulSoup(data['strGrid'],'lxml')


# In[369]:


prods=soup.findAll('a', title=True)
cat_img= soup.findAll('figure',class_='pro1')
# prod_urls= []

# cat_imgs=[]
print(len(prods))
print(len(cat_img))
for urls,img in zip(prods,cat_img):

    imgs =img.get('data-images')


    prod_urls.append(baseurl+urls.get('href'))
    cat_imgs.append(imgs)


# In[370]:


print(len(prod_urls))
print(len(cat_imgs))
print(len(gen))


# In[371]:


import requests

cookies = {
    'ASP.NET_SessionId': 'gggaum2fiuxeejptjabbz1cv',
    'VisiterID': '986a0d87-4032-4983-87a2-a8663ed2bc17',
    '_gcl_au': '1.1.975566304.1668408536',
    '_gid': 'GA1.2.1199791776.1668408537',
    'ln_or': 'd',
    '_fbp': 'fb.1.1668408537270.1196558888',
    '__insp_wid': '1939799058',
    '__insp_nv': 'true',
    '__insp_targlpu': 'aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D',
    '__insp_targlpt': 'U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0',
    '__insp_norec_sess': 'true',
    '_uetsid': '6991c4c063e811ed918e1d3d3c1a5aeb',
    '_uetvid': '6992a9f063e811ed9bb2db5b89275a12',
    '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDI1NTg3LCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=',
    '_ga': 'GA1.2.2070327007.1668408537',
    '_dc_gtm_UA-159937545-2': '1',
    '__insp_slim': '1668425588972',
    '_ga_P2P1R3FERZ': 'GS1.1.1668408536.1.1.1668425592.0.0.0',
}

headers = {
    'authority': 'www.corporategear.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ur;q=0.8,so;q=0.7,hi;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ASP.NET_SessionId=gggaum2fiuxeejptjabbz1cv; VisiterID=986a0d87-4032-4983-87a2-a8663ed2bc17; _gcl_au=1.1.975566304.1668408536; _gid=GA1.2.1199791776.1668408537; ln_or=d; _fbp=fb.1.1668408537270.1196558888; __insp_wid=1939799058; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw%2FYWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWw%3D; __insp_targlpt=U1RJTyBNZW4ncyBQaW5pb24gRG93biBWZXN0IHwgU1RJTyBFbWJyb2lkZXJlZCBWZXN0; __insp_norec_sess=true; _uetsid=6991c4c063e811ed918e1d3d3c1a5aeb; _uetvid=6992a9f063e811ed9bb2db5b89275a12; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDI1NTg3LCJ2YWx1ZSI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vc3Rpby1tZW4tcy1waW5pb24tZG93bi12ZXN0Lmh0bWw/YWx0dmlldz0xJnY9cHJvZHVjdC1kZXRhaWwifX0=; _ga=GA1.2.2070327007.1668408537; _dc_gtm_UA-159937545-2=1; __insp_slim=1668425588972; _ga_P2P1R3FERZ=GS1.1.1668408536.1.1.1668425592.0.0.0',
    'dnt': '1',
    'origin': 'https://www.corporategear.com',
    'referer': 'https://www.corporategear.com/accessories-drinkware.html?v=product-list',
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
    'newcatid': '13878',
    'color': '',
    'size': '',
    'type': '',
    'gender': '',
    'price': '',
    'brand': '',
    'sortby': '',
    'url': '/accessories-drinkware.html',
    'startrow': '1',
    'endrow': '80',
    'guidnew': '601f9056-f1f6-4fac-b9b2-07b681043d9c',
}

response = requests.post('https://www.corporategear.com/Category/Getpaggingdata', cookies=cookies, headers=headers, data=data)


# In[372]:


import json 
from bs4 import BeautifulSoup
from pprint import pprint
data= response.json()
data= json.dumps(data)
data= json.loads(data)
# print(data['strGrid'])
baseurl ="https://www.corporategear.com"
soup = BeautifulSoup(data['strGrid'],'lxml')


# In[373]:


prods=soup.findAll('a', title=True)
cat_img= soup.findAll('figure',class_='pro1')
# prod_urls= []

# cat_imgs=[]
print(len(prods))
print(len(cat_img))
for urls,img in zip(prods,cat_img):

    imgs =img.get('data-images')


    prod_urls.append(baseurl+urls.get('href'))
    cat_imgs.append(imgs)


# In[374]:


print(len(prod_urls))
print(len(cat_imgs))
print(len(gen))


# In[375]:


print(len(set(prod_urls)))
print(len(set(cat_imgs)))


# In[383]:


data_dict= {"Product URLS":prod_urls, "Catalog Images":cat_imgs}


# In[382]:


for url,cata in zip(prod_urls,cat_imgs):
    print(url,cata)


# In[384]:


df = pd.DataFrame.from_dict(data_dict)
import pandas as pd
df= pd.DataFrame.from_dict(data)


# In[ ]:


df


# In[ ]:





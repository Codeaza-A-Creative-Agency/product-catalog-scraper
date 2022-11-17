import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
import re,json
from bs4 import BeautifulSoup
import os
for i in range(1,11):
    df= pd.read_csv(f'Category-{i}-Urls.csv')
    df=df['Product URL'].tolist()
# df = set(df)
# df= list(df)
df= df[0:50]
# df = ["https://www.corporategear.com/eddie-bauer-men-s-fleece-vest.html?v=product-detail"]

class catalog_scraper(scrapy.Spider):
    
    custom_settings = {
        'DOWNLOAD_DELAY' : 0.25,
        'RETRY_TIMES': 10,
        # export as CSV format
        'FEED_FORMAT' : 'csv',
        # 'FEED_URI' : 'all-data.csv'
    #     "ROTATING_PROXY_LIST" : ["108.59.14.208:13040", "108.59.14.203:13040"],
    #             "DOWNLOADER_MIDDLEWARES" : {
    #             "rotating_proxies.middlewares.RotatingProxyMiddleware" : 610,
    #             "rotating_proxies.middlewares.BanDetectionMiddleware" : 620}
    }
     
    name= 'scraper'
    headers = {
            'authority': 'www.corporategear.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ur;q=0.8,so;q=0.7,hi;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'ASP.NET_SessionId=gggaum2fiuxeejptjabbz1cv; VisiterID=986a0d87-4032-4983-87a2-a8663ed2bc17; _gcl_au=1.1.975566304.1668408536; _gid=GA1.2.1199791776.1668408537; ln_or=d; _fbp=fb.1.1668408537270.1196558888; __insp_wid=1939799058; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuY29ycG9yYXRlZ2Vhci5jb20vbWVuLXZlc3RzLmh0bWw%2Fdj1wcm9kdWN0LWxpc3Q%3D; __insp_targlpt=Q3VzdG9tIFZlc3RzICYgTDNEpUTHQoQUJMHLrErGJyHg89uy71MyuHRlcmVkIHdpdGggWW91ciBDb3Jwb3JhdGUgTG9nbw%3D%3D; __insp_norec_sess=true; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2Njg0MDg1MzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmNvcnBvcmF0ZWdlYXIuY29tL21lbi12ZXN0cy5odG1sP3Y9cHJvZHVjdC1saXN0In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjY4NDkzMTIzLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5jb3Jwb3JhdGVnZWFyLmNvbS9tZW4tdmVzdHMuaHRtbD92PXByb2R1Y3QtbGlzdCJ9fQ==; _uetsid=6991c4c063e811ed918e1d3d3c1a5aeb; _uetvid=6992a9f063e811ed9bb2db5b89275a12; _dc_gtm_UA-159937545-2=1; _ga=GA1.2.2070327007.1668408537; _ga_P2P1R3FERZ=GS1.1.1668485378.2.1.1668493124.0.0.0; __insp_slim=1668493124438',
            'dnt': '1',
            'origin': 'https://www.corporategear.com',
            'referer': "https://www.corporategear.com",
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
    def start_requests(self):
        
        for i in range(1,11):
            df= pd.read_csv(f'Category-{i}-Urls.csv')
            df=df['Product URL'].tolist()
            df= df[:10]
            df = ["https://www.corporategear.com/eddie-bauer-men-s-fleece-vest.html?v=product-detail"]
            for url in df:
                yield scrapy.Request(url=url, callback=self.parse, meta={'Cat_num':i})
    
    def parse(self,response):
        msrp_price = response.css("div.label-msrp+div>h2::text").extract_first()

        source_script_data = response.xpath("//div[@class='container']//script[@type='application/ld+json']/text()").extract_first().strip()  
        new_string = re.sub(r"\s+|\\","",source_script_data)
        new_string = new_string.replace('"{"@context','"}},{"@context')
        if not new_string.endswith("}}]"):
            new_string = new_string[:-1] + "}}]"
        json_parsed_data = json.loads(new_string)
        

        # all colors main data
        # unique_colors_data = {}     #{'colorname': {'@context':'....}}
        unique_colors_data = []
        try:
            desc2 =response.xpath("//div[@itemprop='description']//ul//text()").extract()
            desc2 = ''.join(desc2)
        except:
            desc2= ''
        for data in json_parsed_data: 
            if data.get("color") not in unique_colors_data:

                sku = data['sku']
                name= data['name']
                cat_img= data['image']
                desc= data['description']
                brand= data['brand']['name']
                # price= data['offers']['price']
                gender= data['audience']['suggestedGender']
                # size= info['size']
                soup = BeautifulSoup(desc, 'html.parser')
                desc = soup.text
                try:
                    min_ord=response.xpath("(//div[@class='pull-right']/a)[2]/text()").extract()[1]
                    
                except:
                    min_ord =response.xpath("(//div[@class='pull-right']/a/text())").extract()[1]        
                
                data_dict= {}
                data_dict["SKU"]=sku
                data_dict["Product Name"]= name
                data_dict['Brand Name']=brand
                data_dict["Base Category"]=response.xpath("(//li[@class='breadcrumbsdiv']/a/text())[2]").extract_first()
                data_dict['Sub Category']=response.xpath("(//li[@class='breadcrumbsdiv']/a/text())[3]").extract_first()
                data_dict['Description']=desc =response.xpath("//div[@itemprop='description']//p//text()").extract()[0]+ desc2
                data_dict['Catalog Preview Image']=cat_img
                data_dict['MRSP'] = msrp_price
                data_dict['Minimum Order Quantity']=min_ord
                data_dict['Sized']=response.css("h2#allSizes ::text").extract_first()
                data_dict['Gender']=gender
                data_dict['color'] = data.get("color")
                print(data_dict)
                
                # payload = {
                #     'mainimagename': cat_img.split("/")[-1],
                #     'productID': data.get("inProductGroupWithID")
                # }
                payload = f"mainimagename={cat_img.split('/')[-1]}&productID={data.get('inProductGroupWithID')}"

                # yield data_dict
                yield scrapy.Request(url="https://www.corporategear.com/Itempage/GetMoreImagePost",method="POST",headers = self.headers,body=str(payload),callback=self.parse_with_all_images,meta={"all_data" : data_dict, "Cat_num":response.meta['Cat_num']})
        print("Colors: ",unique_colors_data)
    
    def parse_with_all_images(self,response):
        response_data = json.loads(response.text)
        soup = BeautifulSoup(response_data, 'html.parser')

        imgs = soup.findAll('img')
        all_images = [image.get("src") for image in imgs]

        data = {
            **response.meta.get("all_data"),
            "all_images" : all_images
        }

        product_dict = data.copy()
        product_dict.pop('all_images')
        products_dataframe = pd.DataFrame(product_dict)
        
        images_dict = {
            "SKU" : [data.get("SKU")],
            "colorName" : [data.get("color")]
        }
        for i,j in enumerate(data.get("all_images")):
            images_dict[f"image{i}"] = [j]

        images_dataframe = pd.DataFrame(images_dict)
        print(images_dataframe)

        if os.path.exists(os.path.join(os.getcwd(),f"Sample-Records-{response.meta['Cat_num']}.xlsx")):
            with pd.ExcelWriter("Sample-Records-1.xlsx",mode='a',if_sheet_exists='overlay',engine='openpyxl') as writer:
                
                startroww = writer.sheets['products'].max_row
                products_dataframe.to_excel(writer,startrow=startroww,index=False,header=False,sheet_name="products")
                
                startroww = writer.sheets['Colors'].max_row
                images_dataframe.to_excel(writer,startrow=startroww,index=False,header=False,sheet_name="Colors")

        else:
            with pd.ExcelWriter(f"Sample-Records-{response.meta['Cat_num']}.xlsx") as writer:
                products_dataframe.to_excel(writer,index=False,sheet_name="products")
                images_dataframe.to_excel(writer,index=False,sheet_name="Colors")


        # data = {
        #     **response.meta.get("all_data")
        #     # "all_images" : all_images
        # }

        # for i,j in enumerate(all_images):
        #     data[f"image{i}"] = j
        

        # yield data


        # product_dict = data.copy()
        # product_dict.pop('all_images')
        # products_dataframe = pd.DataFrame(product_dict)
        
        # images_dict = {
        #     "SKU" : [data.get("SKU")],
        #     "colorName" : [data.get("color")]
        # }
        # for i,j in enumerate(data.get("all_images")):
        #     images_dict[f"image{i}"] = [j]

        # images_dataframe = pd.DataFrame(images_dict)

        # if os.path.exists(os.path.join(os.getcwd(),"Sample-Records.xlsx")):
        #     with pd.ExcelWriter("Sample-Records.xlsx",mode='a',if_sheet_exists='overlay',engine='openpyxl') as writer:
        #         startroww = writer.sheets['products'].max_row
        #         products_dataframe.to_excel(writer,startrow=startroww,index=False,header=False,sheet_name="products")
                
        #         # startroww = writer.sheets['Colors'].max_row
        #         # images_dataframe.to_excel(writer,startrow=startroww,index=False,header=False,sheet_name="Colors")

        # else:
        #     products_dataframe.to_excel("Sample-Records.xlsx",index=False,sheet_name="products")
        #     # images_dataframe.to_excel("Sample-Records.xlsx",index=False,sheet_name="Colors")


        # print(data)
        # pass

    
process = CrawlerProcess()
process.crawl(catalog_scraper)
process.start()
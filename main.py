import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
import re,json
from bs4 import BeautifulSoup

df= pd.read_csv('prods-1.csv')
df=df['Product URL'].tolist()
df = set(df)
df= list(df)
df= df[0:50]

class catalog_scraper(scrapy.Spider):
    
    custom_settings = {
        'DOWNLOAD_DELAY' : 0.25,
        'RETRY_TIMES': 10,
        # export as CSV format
        'FEED_FORMAT' : 'csv',
        'FEED_URI' : 'prod_catalog_sample_data.csv'
    #     "ROTATING_PROXY_LIST" : ["108.59.14.208:13040", "108.59.14.203:13040"],
    #             "DOWNLOADER_MIDDLEWARES" : {
    #             "rotating_proxies.middlewares.RotatingProxyMiddleware" : 610,
    #             "rotating_proxies.middlewares.BanDetectionMiddleware" : 620}
    }
     
    name= 'scraper'
    def start_requests(self):
        for url in df:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self,response):
        source_script_data = response.xpath("//div[@class='container']//script[@type='application/ld+json']/text()").extract_first().strip()  
        new_string = re.sub(r"\s+|\\","",source_script_data)
        new_string = new_string.replace('"{"@context','"}},{"@context')
        if not new_string.endswith("}}]"):
            new_string = new_string[:-1] + "}}]"
        json_parsed_data = json.loads(new_string)
        print(len(json_parsed_data))
        for info in json_parsed_data:
            sku = info['sku']
            name= info['name']
            cat_img= info['image']
            desc= info['description']
            brand= info['brand']['name']
            price= info['offers']['price']
            gender= info['audience']['suggestedGender']
            size= info['size']
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
            data_dict['Description']=desc,
            data_dict['Catalog Preview Image']=cat_img
            data_dict['MRSP']=price
            data_dict['Minimum Order Quantity']=min_ord
            data_dict['Sized']=response.css("h2#allSizes ::text").extract_first()
            data_dict['Gender']=gender
            yield data_dict
    
        
   
    
    


process = CrawlerProcess()
process.crawl(catalog_scraper)
process.start()
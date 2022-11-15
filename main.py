import scrapy 
from scrapy.crawler import CrawlerProcess
import pandas as pd
df= pd.read_csv('prods-1.csv')
df=df['Product URL']

class catalog_scraper(scrapy.Spider):
    
    custom_settings = {
        'DOWNLOAD_DELAY' : 0.25,
        'RETRY_TIMES': 10,
        # export as CSV format
        'FEED_FORMAT' : 'csv',
        # 'FEED_URI' : 'testing.csv'
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
        
        sc =response.xpath("//div[@class='container']//script[@type='application/ld+json']/text()").extract_first().strip().replace("]","}]")
        
        data_dict= {}
        data_dict["SKU"]=''
        data_dict["Product Name"]= ''
        data_dict['Brand Name']=''
        data_dict["Base Category"]=''
        data_dict['Sub Category']='',
        data_dict['Description']=''
        data_dict['Catalog Preview Image']=''
        data_dict['MRSP']=''
        data_dict['Minimum Order Quantity']=''
        data_dict['Sized']=''
        data_dict['Gender']=''
        print(response.url)
   
        
      
 
    
    


process = CrawlerProcess()
process.crawl(catalog_scraper)
process.start()
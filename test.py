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
        data_dict["SKU"]=response.xpath("//span[@itemprop='mpn']/text()").extract_first()
        data_dict["Product Name"]= response.xpath("//div[@class='item-title hidden-sm hidden-xs']/h1/text()").extract_first()
        data_dict['Brand Name']=response.xpath("(//a[@id='abreadcrumb_1']/text())[3]").extract_first()
        data_dict["Base Category"]=response.xpath("(//li[@class='breadcrumbsdiv']/a/text())[2]").extract_first()
        data_dict['Sub Category']=response.xpath("(//li[@class='breadcrumbsdiv']/a/text())[3]").extract_first(),
        data_dict['Description']=response.xpath("//div[@class='readmore']/text()").extract()
        data_dict['Catalog Preview Image']=''
        data_dict['MRSP']=response.xpath("(//div[@class='span']/h2/text())[2]").extract_first()
        data_dict['Minimum Order Quantity']=response.xpath("//strong[contains(text(),'MINIMUM')]/text()").extract_first()
        data_dict['Sized']=response.css("h2#allSizes ::text").extract_first()
        data_dict['Gender']=''
        print(response.url)
   
        
      
 
    
    


process = CrawlerProcess()
process.crawl(catalog_scraper)
process.start()
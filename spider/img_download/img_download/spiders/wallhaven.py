import scrapy
from img_download.items import ImgDownloadItem

class WallhavenSpider(scrapy.Spider):
    name = 'wallhaven'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['http://wallhaven.cc/']
    def parse(self, response):
        temp=response.xpath('//*[@id="featured"]/div[5]/div/span');
        for i in temp:
            url=i.xpath('./a/img/@src').extract();
            item=ImgDownloadItem(img_url=url[0]);
            yield item;
            # print(item);




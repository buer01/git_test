# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import  ImagesPipeline
import os
class ImgDownloadPipeline(ImagesPipeline):
    number=1;
    def get_media_requests(self, item, info):
        img_url=item['img_url'];
        yield scrapy.Request(img_url);

    def item_completed(self, results, item, info):
        print(results);
        path='D:/python/projec_git/spider/img_download/image/'
        if(results[0][0]==True):
            os.rename(path+results[0][1]['path'],path+'full/'+str(self.number)+'.jpg');
            self.number+=1;


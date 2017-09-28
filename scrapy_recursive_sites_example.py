import scrapy
from scrapy.crawler import CrawlerProcess

class TrainSpider(scrapy.Spider):
    name = "trip"
    start_urls = ['http://baike.wdzj.com/list-letter-a-1.html']
    def parse(self, response):
        ''' do something with this parser '''
        next_page = response.xpath('//div[@id="fenye"]/a[contains(text(),"››")]/@href').extract_first()
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(TrainSpider)
process.start() # the script will block here until the crawling is finished


# %%
# import scrapy
# from scrapy.crawler import CrawlerProcess
#
# class TrainSpider()

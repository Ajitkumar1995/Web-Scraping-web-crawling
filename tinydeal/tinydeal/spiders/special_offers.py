# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com']
    #start_urls = ['https://www.tinydeal.com/specials.html']
    
    def start_requests(self):
        yield scrapy.Requestscrapy(url='https://www.tinydeal.com/specials.html',callback=self.parse,heardes={
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36'
        })
    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            yield{
                'title':product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url':response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discounted_price':product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
                'original_price':product.xpath(".//div[@class='p_box_price']/span[2]/text()").get(),
                'User-Agent':response.request.headers['User-Agent']
            }
        next_page=response.xpath("//a[@class='next_page']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse,heardes={
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36'})
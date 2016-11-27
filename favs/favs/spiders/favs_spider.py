import scrapy


class FavsSpider(scrapy.Spider):
    name = "favs"
    start_urls = ['https://habrahabr.ru/users/stleon/favorites/', ]

    def parse(self, response):

        for href in response.xpath(
                '//a[contains(@class, "post__title_link")]/@href').extract():
            yield scrapy.Request(
                response.urljoin(href), callback=self.parse_topic)

        next_page = response.xpath('//a[@id="next_page"]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_topic(self, response):
        tags = response.xpath(
            './/div[@class="post__tags"]/ul/li//a/text()').extract()
        for tag in tags:
            self.log(tag)

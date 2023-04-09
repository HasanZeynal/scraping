import scrapy


class PopularSpider(scrapy.Spider):
    name = "popular"
    allowed_domains = ["www.goodreads.com/quotes"]
    start_urls = ["https://www.goodreads.com/quotes"]

    def parse(self, response):
        quotes = response.xpath("//div[@class='quotes']/div")
        for quote in quotes:
            sentence = quote.xpath('.//div[@class="quoteText"]/text()').getall()
            author_name = quote.xpath('.//span[@class="authorOrTitle"]/text()').getall()
            number_of_likes = quote.xpath(".//a[@class='smallText']/text()").getall()
            tags = quote.xpath('.//div[@class="greyText smallText left"]/a/text()').getall()
            image_links = quote.xpath('.//a[@class="leftAlignedImage"]/img/@src').getall()

            yield{
                'sentence':sentence,
                'author name':author_name,
                'likes':number_of_likes,
                'tags':tags,
                'image link':image_links
            }
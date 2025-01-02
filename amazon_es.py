import scrapy


class AmazonEsSpider(scrapy.Spider):
    name = "amazon_es"
    allowed_domains = ["amazon.es"]
    start_urls = ["https://www.amazon.es/gp/bestsellers/books"]

    def parse(self, response):
        # XPath simplificado para encontrar todos los libros
        books = response.xpath('//div[contains(@class, "uncoverable")]')

        # Procesar cada libro encontrado
        for book in books:
            photo = book.xpath('.//img//@src').get()
            title = book.xpath('.//following-sibling::div//a//span//div//text()').get()
            price = book.xpath('.//span[contains(@class, "price")]//text()').get()
            author = book.xpath('.//following-sibling::div/div//following-sibling::div/span[contains(@class, "base")]//text()').get()
            stars = book.xpath('.//following-sibling::div//a[contains(@title, "calificaciones")]/span//text()').get()

            if title and price and author and stars:
                yield {
                    'photo': photo.strip(),
                    'title': title.strip(),
                    'price': price.strip(),
                    'author': author.strip(),
                    'stars': stars.strip()
                }
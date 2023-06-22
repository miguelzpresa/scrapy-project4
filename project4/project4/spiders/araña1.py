#!/usr/bin/python3
import scrapy
from urllib.parse import urljoin
from scrapy_playwright.page import PageCoroutine
class CIAFactbookSpider(scrapy.Spider):
    name = 'araña1'
    start_urls = ['https://www.cia.gov/the-world-factbook/countries/afghanistan/']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_playwright.middlewares.PlaywrightRequestMiddleware': 610,
        },
        'PLAYWRIGHT_BROWSER': 'chromium',
        'PLAYWRIGHT_LAUNCH_OPTIONS': {'headless': True},
    }


    def start_requests(self):
        yield scrapy.Request(
            start_urls = ['https://www.cia.gov/the-world-factbook/countries/'],

            meta={"playwright":True}

        )


        
    async def parse(self, response):
        country_urls = []
        div_elem = response.xpath('//div[@class="col-lg-9"]')
        
        for div in div_elem:
            country_link = div.xpath('.//a[@class="inline-link"]')
            if country_link:
                country = country_link.xpath('./@href').get()[30:]
                country_url = urljoin(response.url, country)
                country_urls.append(country_url)

        print(country_urls)

        async with PageCoroutine() as page:
            await page.goto(response.url)
            await page.click('//*[@id="index-content-section"]/div/div[2]/div[2]/div/div/span[3]')

>>>>>>> 8e726c6e2a18e307d43ac5d542cf02b43ebaf015
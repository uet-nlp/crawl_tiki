from lxml import html
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
os.chdir('D:\Documents\Code\crawl_tiki')


class HtmlGetter:

    def get_html(self, url):
        pass


class HtmlParseGetter(HtmlGetter):

    def __init__(self, subject):
        self.subject = subject

    def get_html(self, url):
        html_source = self.subject.get_html(url)
        html_element = html.fromstring(html_source)
        return html_element


class SeleniumHtmlGetter(HtmlGetter):
    def __init__(self, scroll_to_bottom=True):
        self.scroll_to_bottom = scroll_to_bottom

    def get_html(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument("./chromedriver.exe")
        options.add_argument('--headless')
        # options.add_argument('--incognito')
        # options.add_argument('--window-size=1200x800')
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        if self.scroll_to_bottom:
            last = None
            for v in range(500):
                for k in range(5):
                    driver.find_element_by_xpath('//html').send_keys(Keys.DOWN)
                if last is not None and last == driver.execute_script('return window.pageYOffset;'):
                    break
                last = driver.execute_script('return window.pageYOffset;')

        html_source = driver.page_source
        driver.quit()
        return html_source


if __name__ == '__main__':
    url = 'https://tiki.vn/deal-hot'
    html_getter = HtmlParseGetter(SeleniumHtmlGetter(scroll_to_bottom=True))
    html_tree = html_getter.get_html(url)

    tree = html_tree.xpath("//div[@class='Item__Wrapper-m1oy8w-0 bYqVDW']")
    for v in tree:
        with open('tiki_sale.csv','a', encoding='utf-8', newline='') as csvfile:
            a = v.xpath(".//div[@class='title deal']/text()")[0] if len(v.xpath(".//div[@class='title deal']/text()")) != 0 else ''
            b = v.xpath(".//p[@class='price deal']/text()")[0] if len(v.xpath(".//p[@class='price deal']/text()")) != 0 else ''
            c = v.xpath(".//span[@class='percent deal']/text()")[0] if len(v.xpath(".//span[@class='percent deal']/text()")) != 0 else ''
            d = v.xpath(".//span[@class='original deal']/text()")[0] if len(v.xpath(".//span[@class='original deal']/text()")) != 0 else ''
            e = v.xpath(".//a/@href")[0] if len(v.xpath(".//a/@href")) != 0 else ''
            data = ([a,b,c,d,e])

            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(data) 
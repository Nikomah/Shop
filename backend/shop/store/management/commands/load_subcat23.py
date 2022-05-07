import shutil

import requests
from django.core.files import File
from django.core.management import BaseCommand

from shop.settings import BASE_DIR
from store.models import Product, Subcategory, Subcat2, Subcat3
from bs4 import BeautifulSoup


class Command(BaseCommand):
    SUB4_DICT = {}
    url = 'https://maloni.ru'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                  '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    def handle(self, *args, **options):
        resp = requests.get(self.url, headers=self.header)
        if resp.status_code == 200:
            main_page = BeautifulSoup(resp.text, 'html.parser')
            sidebar = main_page.find(id='sidebar')
            categories = sidebar.find_all('li')
            for li in categories:
                subcat_url = li.a['href']
                self.get_subcategory(self.url+subcat_url)

    def get_subcategory(self, sub_url):
        resp = requests.get(sub_url, headers=self.header)
        subcat_page = BeautifulSoup(resp.text, 'html.parser')
        catalog_list = subcat_page.find(id='same-height')
        if catalog_list:
            subcategories = catalog_list.find_all('li')
            for li in subcategories:
                subcategory = li.find('a').text.strip()
                subcat2_url = li.a['href']
                subcat = Subcategory.objects.get(name=subcategory)
                self.get_subcat2(self.url+subcat2_url, subcat.pk)

    def get_subcat2(self, sub2_url, subcategory: int):
        resp = requests.get(sub2_url, headers=self.header)
        subcat2_page = BeautifulSoup(resp.text, 'html.parser')
        catalog_list = subcat2_page.find(id='same-height')
        if catalog_list:
            subcat2s = catalog_list.find_all('li')
            for li in subcat2s:
                subcat3_url = li.a['href']
                subcat2 = Subcat2.objects.get(name=li.a['title'])
                subcat2 = Subcat2()
                subcat2.name = li.a['title']
                image_url = self.url + li.img['src']
                img_response = requests.get(image_url, stream=True)
                with open('tmp.png', 'wb') as out_file:
                    shutil.copyfileobj(img_response.raw, out_file)
                with open('%s/tmp.png' % BASE_DIR, 'rb') as image_file:
                    subcat2.image.save('subcat2.png', File(image_file), save=True)
                subcat2.subcategory_id = subcategory
                subcat2.save()
                self.get_subcat3_and_product(self.url+subcat3_url, subcat2.pk)

    def get_subcat3_and_product(self, sub3_url, subcat2):
        resp = requests.get(sub3_url, headers=self.header)
        subcat2_page = BeautifulSoup(resp.text, 'html.parser')
        catalog_list = subcat2_page.find(id='same-height')
        self.get_prod_of_sub3(catalog_list, subcat2)
        self.get_sub3(catalog_list, subcat2)

    def get_prod_of_sub3(self, catalog_list, subcat2):
        products_image = catalog_list.find_all('div', attrs={'class': 'tov-img'})
        products_price = catalog_list.find_all('div', attrs={'class': 'price-block'})
        products_quantity = catalog_list.find_all('div', attrs={'class': 'surplus'})
        for product in products_image:
            prod = Product()
            prod.name = product.img['title']
            img_url = self.url + product.img['src']
            img_response = requests.get(img_url, stream=True)
            with open('tmp.png', 'wb') as out_file:
                shutil.copyfileobj(img_response.raw, out_file)
            with open('%s/tmp.png' % BASE_DIR, 'rb') as image_file:
                prod.image.save('prod.png', File(image_file), save=True)
            prod.subcat2_id = subcat2
            for product_p in products_price:
                if not prod.price:
                    try:
                        prod.price = float((product_p.find(id='lpr').text.split()[0]).replace(',', '.'))
                    except ValueError:
                        pass
            products_price.pop(0)
            for product_q in products_quantity:
                if not prod.quantity:
                    try:
                        prod.quantity = int((product_q.find('span', class_='on_storages').text.split()[0]))
                    except AttributeError:
                        pass
            products_quantity.pop(0)
            prod.save()

    def get_sub3(self, catalog_list, subcat2):
        subcat3s = catalog_list.find_all('li')
        for li in subcat3s:
            subcat4_url = li.a['href']
            subcat3 = Subcat3()
            subcat3.name = li.a['title']
            image_url = self.url + li.img['src']
            img_response = requests.get(image_url, stream=True)
            with open('tmp.png', 'wb') as out_file:
                shutil.copyfileobj(img_response.raw, out_file)
            with open('%s/tmp.png' % BASE_DIR, 'rb') as image_file:
                subcat3.image.save('subcat3.png', File(image_file), save=True)
            subcat3.subcat2_id = subcat2
            subcat3.save()

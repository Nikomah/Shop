import shutil

import requests
from django.core.files import File
from django.core.management import BaseCommand

from shop.settings import BASE_DIR
from store.models import Product, Subcategory, Category
from bs4 import BeautifulSoup


class Command(BaseCommand):
    url = 'https://maloni.ru'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                  '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    def get_product(self, prod_url, subcategory: int):
        resp = requests.get(prod_url, headers=self.header)
        if resp.status_code == 200:
            prod_page = BeautifulSoup(resp.text, 'html.parser')
            prod_list = prod_page.find(id='same-height')
            products_image = prod_list.find_all('div', attrs={'class': 'tov-img'})
            products_price = prod_list.find_all('div', attrs={'class': 'price-block'})
            products_quantity = prod_list.find_all('div', attrs={'class': 'surplus'})
            for product in products_image:
                prod = Product()
                prod.name = product.img['title']
                img_url = self.url+product.img['src']
                img_response = requests.get(img_url, stream=True)
                # сохраняем временный файл
                with open('tmp.png', 'wb') as out_file:
                    shutil.copyfileobj(img_response.raw, out_file)
                # читаем временный файл и загружаем его программно в модель
                with open('%s/tmp.png' % BASE_DIR, 'rb') as image_file:
                    prod.image.save('prod.png', File(image_file), save=True)
                prod.subcategory_id = subcategory
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
        else:
            print(resp.status_code)

    def get_subcategory(self, sub_url, category: int):
        resp = requests.get(sub_url, headers=self.header)
        if resp.status_code == 200:
            subcat_page = BeautifulSoup(resp.text, 'html.parser')
            catalog_list = subcat_page.find(id='same-height')
            if catalog_list:
                subcategories = catalog_list.find_all('li')
                for li in subcategories:
                    subcategory = li.find('a').text.strip()
                    subcat = Subcategory()
                    subcat.name = subcategory
                    subcat.category_id = category
                    subcat.save()
                    prod_url = li.a['href']
                    self.get_product(self.url+prod_url, subcat.pk)

    def get_category(self):
        resp = requests.get(self.url, headers=self.header)
        if resp.status_code == 200:
            main_page = BeautifulSoup(resp.text, 'html.parser')
            sidebar = main_page.find(id='sidebar')
            categories = sidebar.find_all('li')
            for li in categories:
                category = li.find('a').text
                subcat_url = li.a['href']
                cat = Category()
                cat.name = category
                cat.save()
                self.get_subcategory(self.url+subcat_url, cat.pk)

    def handle(self, *args, **options):
        print('Clearig Data Base')
        # удаляем записи из бд и картинки
        Product.objects.all().delete()
        Subcategory.objects.all().delete()
        Category.objects.all().delete()
        try:
            shutil.rmtree('%s/media/images' % BASE_DIR)
        except:
            pass
        # достаём страницу из вэб и парсим
        print('Start importing from %s' % self.url)
        self.get_category()

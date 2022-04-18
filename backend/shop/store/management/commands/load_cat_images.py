import shutil

import requests
from django.core.files import File
from django.core.management import BaseCommand

from shop.settings import BASE_DIR
from store.models import Category
from bs4 import BeautifulSoup


class Command(BaseCommand):
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
            sidebar = main_page.find(id='same-height')
            categories = sidebar.find_all('li')
            for li in categories:
                category_img = li.img
                if category_img:
                    category_name = category_img['title']
                    cat = Category.objects.get(name=category_name)
                    img_url = self.url + category_img['src']
                    img_response = requests.get(img_url, stream=True)
                    with open('tmp.png', 'wb') as out_file:
                        shutil.copyfileobj(img_response.raw, out_file)
                    with open('%s/tmp.png' % BASE_DIR, 'rb') as image_file:
                        cat.image.save('cat.png', File(image_file), save=True)

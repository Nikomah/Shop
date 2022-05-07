import shutil

import requests
from django.core.files import File
from django.core.management import BaseCommand

from shop.settings import BASE_DIR
from store.models import Product, Subcat3, Subcat4
from bs4 import BeautifulSoup


class Command(BaseCommand):
    url = 'https://maloni.ru'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                  '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    SUB4_URLS = {'Профлист С-8 оцинкованный': '/cat/zabory-i-krovlya/proflist/proflist-s-8/proflist-s8-cynk/',
                 'Профлист С-8 вишневый': '/cat/zabory-i-krovlya/proflist/proflist-s-8/proflist-s8-krasnyi/',
                 'Профлист С-8 зеленый': '/cat/zabory-i-krovlya/proflist/proflist-s-8/proflist-s8-zelenyi/',
                 'Профлист С-8 коричневый': '/cat/zabory-i-krovlya/proflist/proflist-s-8/proflist-s8-korichnevyi/',
                 'Профлист С-21 оцинкованный': '/cat/zabory-i-krovlya/proflist/proflist-s-21/proflist-s21-cynk/',
                 'Профлист С-21 вишневый': '/cat/zabory-i-krovlya/proflist/proflist-s-21/proflist-s21-krasnyi/',
                 'Профлист С-21 зеленый': '/cat/zabory-i-krovlya/proflist/proflist-s-21/proflist-s21-zelenyi/',
                 'Профлист С-21 коричневый': '/cat/zabory-i-krovlya/proflist/proflist-s-21/proflist-s21-korichnevyi/',
                 'Крюк': '/cat/krepej_i_instrumenty/krepej/takelag/kryuk/',
                 'Коуш': '/cat/krepej_i_instrumenty/krepej/takelag/koush/',
                 'Талреп крюк-кольцо': '/cat/krepej_i_instrumenty/krepej/takelag/talrep-kryuk-koltso/',
                 'Соединитель цепей': '/cat/krepej_i_instrumenty/krepej/takelag/soedinitel-tsepei/',
                 'Рым-гайка': '/cat/krepej_i_instrumenty/krepej/takelag/rym-gaika/',
                 'Рым-болт': '/cat/krepej_i_instrumenty/krepej/takelag/rym-bolt/',
                 'Карабин': '/cat/krepej_i_instrumenty/krepej/takelag/karabin/',
                 'Зажим SIMPLEX': '/cat/krepej_i_instrumenty/krepej/takelag/zagim-simplex/',
                 'Зажим канатный': '/cat/krepej_i_instrumenty/krepej/takelag/zagim-kanatnyi/',
                 'Тросы': '/cat/krepej_i_instrumenty/krepej/takelag/trosy/',
                 'Цепи': '/cat/krepej_i_instrumenty/krepej/takelag/tsepi/',
                 'Анкера рамные': '/cat/krepej_i_instrumenty/krepej/ankera/ankera-ramnye/',
                 'Гвозди строительные': '/cat/krepej_i_instrumenty/krepej/gvozdi/stroitelnye/',
                 'Гвозди ершеные': '/cat/krepej_i_instrumenty/krepej/gvozdi/ershenye/',
                 'Гвозди винтовые': '/cat/krepej_i_instrumenty/krepej/gvozdi/vintovye/',
                 'Гвозди шиферные': '/cat/krepej_i_instrumenty/krepej/gvozdi/shifernye/',
                 'Гвозди толевые': '/cat/krepej_i_instrumenty/krepej/gvozdi/tolevye/',
                 'Гвозди финишные': '/cat/krepej_i_instrumenty/krepej/gvozdi/finishnye/',
                 'Саморезы по дереву': '/cat/krepej_i_instrumenty/krepej/samorezy/samorezy-po-derevu/',
                 'Саморезы по металлу': '/cat/krepej_i_instrumenty/krepej/samorezy/samorezy-po-metallu/',
                 'Саморезы по ГВЛ': '/cat/krepej_i_instrumenty/krepej/samorezy/samorezy-po-gvl/',
                 'Саморезы с прессшайбой, острые': '/cat/krepej_i_instrumenty/krepej/samorezy/samorezy-s-press-shaiboi-ostrye/',
                 'Саморезы с прессшайбой, сверло': '/cat/krepej_i_instrumenty/krepej/samorezy/samorezy-s-press-shaiboi-sverlo/',
                 'Саморезы окрашенные с прессшайбой': '/cat/krepej_i_instrumenty/krepej/samorezy/samorezy-okrashennye-s-pressshaiboi/',
                 'Саморезы кровельные': '/cat/krepej_i_instrumenty/krepej/samorezy/samorezy-krovelnye/',
                 'Шурупы': '/cat/krepej_i_instrumenty/krepej/samorezy/shurupy/',
                 'Биты Ph': '/cat/krepej_i_instrumenty/krepej/bity/bity-ph/',
                 'Биты Pz': '/cat/krepej_i_instrumenty/krepej/bity/bity-pz/',
                 'Биты шестигранные': '/cat/krepej_i_instrumenty/krepej/bity/bity-shestigrannye/',
                 'Адаптеры, переходники': '/cat/krepej_i_instrumenty/krepej/bity/adaptery-perehodniki/',
                 'Дюбель пластмассовый': '/cat/krepej_i_instrumenty/krepej/dubeli/dubel-plastmassovyi/',
                 'Дюбель тип U (желтый)': '/cat/krepej_i_instrumenty/krepej/dubeli/dubel-tip-u/',
                 'Для гипсокартона': '/cat/krepej_i_instrumenty/krepej/dubeli/dubel-dlya-gipsokartona/',
                 'Для пенобетона': '/cat/krepej_i_instrumenty/krepej/dubeli/dubel-dlya-penobetona/',
                 'Для газобетона': '/cat/krepej_i_instrumenty/krepej/dubeli/dubel-dlya-gazobetona/',
                 'Дюбели с шурупами (поштучно)': '/cat/krepej_i_instrumenty/krepej/dubeli-s-shurupami/dubeli-s-shurupami-sht/',
                 'Дюбели с шурупами в коробке': '/cat/krepej_i_instrumenty/krepej/dubeli-s-shurupami/dubeli-s-shurupami-v-korobke/',
                 'Дюбели с шурупами (фасовка)': '/cat/krepej_i_instrumenty/krepej/dubeli-s-shurupami/dubeli-s-shurupami-fasovka/',
                 'Анкера регулируемые': '/cat/krepej_i_instrumenty/krepej/perforacya/ankera-reguliruemye/',
                 'Держатели балки': '/cat/krepej_i_instrumenty/krepej/perforacya/dergateli-balki/',
                 'Пластина гвоздевая': '/cat/krepej_i_instrumenty/krepej/perforacya/plastina-gvozdevaya/',
                 'Опора стропил скользящая': '/cat/krepej_i_instrumenty/krepej/perforacya/opora-stropil-skolzyaschaya/',
                 'Опора балки': '/cat/krepej_i_instrumenty/krepej/perforacya/opora-balki/',
                 'Опора бруса': '/cat/krepej_i_instrumenty/krepej/perforacya/opora-brusa/',
                 'Пластины крепежные': '/cat/krepej_i_instrumenty/krepej/perforacya/plastiny-krepegnye/',
                 'Пластины соединительные': '/cat/krepej_i_instrumenty/krepej/perforacya/plastiny-soedinitelnye/',
                 'Уголки KUL': '/cat/krepej_i_instrumenty/krepej/perforacya/ugolki-kul/',
                 'Уголки KUR': '/cat/krepej_i_instrumenty/krepej/perforacya/ugolki-kur/',
                 'Уголки KUU': '/cat/krepej_i_instrumenty/krepej/perforacya/ugolki-kuu/',
                 'Уголки KUS': '/cat/krepej_i_instrumenty/krepej/perforacya/ugolki-kus/',
                 'Уголки KUZ': '/cat/krepej_i_instrumenty/krepej/perforacya/ugolki-kuz/',
                 'Заглушки': '/cat/krepej_i_instrumenty/krepej/krepeg-dlya-dereva/zaglushki/',
                 'Пробки': '/cat/krepej_i_instrumenty/krepej/krepeg-dlya-dereva/probki/',
                 'Шканты': '/cat/krepej_i_instrumenty/krepej/krepeg-dlya-dereva/shkanty/',
                 'Нагель': '/cat/krepej_i_instrumenty/krepej/krepeg-dlya-dereva/nageli/'}

    def handle(self, *args, **options):
        for name, url in self.SUB4_URLS.items():
            resp = requests.get(self.url + url, headers=self.header)
            subcat4_page = BeautifulSoup(resp.text, 'html.parser')
            catalog_list = subcat4_page.find(id='same-height')

            products_image = catalog_list.find_all('div', attrs={'class': 'tov-img'})
            products_price = catalog_list.find_all('div', attrs={'class': 'price-block'})
            products_quantity = catalog_list.find_all('div', attrs={'class': 'surplus'})
            subcat3 = Subcat3.objects.get(name=name)

            for product in products_image:
                prod = Product()
                prod.name = product.img['title']
                img_url = self.url + product.img['src']
                img_response = requests.get(img_url, stream=True)
                with open('tmp.png', 'wb') as out_file:
                    shutil.copyfileobj(img_response.raw, out_file)
                with open('%s/tmp.png' % BASE_DIR, 'rb') as image_file:
                    prod.image.save('prod.png', File(image_file), save=True)
                prod.subcat3_id = subcat3.pk
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

            subcat4s = catalog_list.find_all('li')
            for li in subcat4s:
                final_prod_url = li.a['href']
                subcat4 = Subcat4()
                subcat4.name = li.a['title']
                image_url = self.url + li.img['src']
                img_response = requests.get(image_url, stream=True)
                with open('tmp.png', 'wb') as out_file:
                    shutil.copyfileobj(img_response.raw, out_file)
                with open('%s/tmp.png' % BASE_DIR, 'rb') as image_file:
                    subcat4.image.save('subcat4.png', File(image_file), save=True)
                subcat4.subcat3_id = subcat3.pk
                subcat4.save()

                resp = requests.get(self.url + final_prod_url, headers=self.header)
                subcat4_page = BeautifulSoup(resp.text, 'html.parser')
                catalog_list = subcat4_page.find(id='same-height')
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
                    prod.subcat4_id = subcat4.pk
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

import random
from random import randint

from config import wsgi
import json
from core.pos.models import *
from core.user.models import User

user = User()
user.username = 'admin'
user.first_name = 'William Jair'
user.last_name = 'Dávila Vargas'
user.email = 'williamjair94@hotmail.com'
user.set_password('admin123')
user.is_superuser = True
user.save()
print('Usuario creado correctamente')

company = Company()
company.name = 'APOLO S.A.'
company.ruc = '0928363212121'
company.address = 'Milagro, Ecuador'
company.mobile = '0979014552'
company.website = 'https://algorisoft.com'
company.save()
print('Compañia creado correctamente')


def insert_products():
    with open(f'{settings.BASE_DIR}/deploy/json/products.json', encoding='utf8') as json_file:
        data = json.load(json_file)
        for p in data['rows'][0:100]:
            row = p['value']
            category = Category.objects.filter(name=row['marca'])
            if not category.exists():
                category = Category()
                category.name = row['marca']
                category.desc = 's/n'
                category.save()
            else:
                category = category[0]
            name = row['nombre']
            while Product.objects.filter(name=name).exists():
                name = f'{name} - {randint(1, 100)}'
            p = Product()
            p.name = name
            p.category_id = category.id
            p.pvp = randint(1, 10)
            p.stock = randint(5, 100)
            p.save()
            print(p.name)


def insert_sale():
    client = Client()
    client.names = 'Consumidor final'
    client.dni = '9999999999'
    client.address = 'Milagro, cdla. Dager avda tumbez y zamora'
    client.save()
    for i in range(1, 11):
        sale = Sale()
        sale.client_id = 1
        sale.iva = 0.12
        sale.save()
        for d in range(1, 8):
            numberList = list(Product.objects.filter(stock__gt=0).values_list(flat=True))
            detail = SaleProduct()
            detail.sale_id = sale.id
            detail.product_id = random.choice(numberList)
            while sale.saleproduct_set.filter(product_id=detail.product_id).exists():
                detail.product_id = random.choice(numberList)
            detail.cant = randint(1, detail.product.stock)
            detail.price = detail.product.pvp
            detail.subtotal = float(detail.price) * detail.cant
            detail.save()
            detail.product.stock -= detail.cant
            detail.product.save()

        sale.calculate_invoice()
        print(i)


insert_products()
insert_sale()

from decimal import Decimal
from django.conf import settings
from shop.models import Product
from .models import Kargo


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price), 'agırlık':str(product.agırlık)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            item['agırlık'] = Decimal(item['agırlık'])
            item['total_agırlık'] = item['agırlık'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
	
    def get_total_kargo(self):
        toplam_agırlık = sum(Decimal(item['agırlık']) * item['quantity'] for item in self.cart.values())
        kargo = Kargo.objects.first()
        if  kargo.agırlık1 <= toplam_agırlık < kargo.agırlık2:
            return kargo.fiyat1
        if  kargo.agırlık2 <= toplam_agırlık < kargo.agırlık3:
            return kargo.fiyat2
        if  kargo.agırlık3 <= toplam_agırlık < kargo.agırlık4:
            return kargo.fiyat3
        if  kargo.agırlık4 <= toplam_agırlık < kargo.agırlık5:
            return kargo.fiyat4
        if  kargo.agırlık5 <= toplam_agırlık < kargo.agırlık6:
            return kargo.fiyat5
        if  kargo.agırlık6 <= toplam_agırlık < kargo.agırlık7:
            return kargo.fiyat6
        if  kargo.agırlık7 <= toplam_agırlık < kargo.agırlık8:
            return kargo.fiyat7
        if  kargo.agırlık8 <= toplam_agırlık < kargo.agırlık9:
            return kargo.fiyat8
        if  kargo.agırlık9 <= toplam_agırlık < kargo.agırlık10:
            return kargo.fiyat9
        if  kargo.agırlık10 <= toplam_agırlık < kargo.agırlık11:
            return kargo.fiyat10
        if  kargo.agırlık11 <= toplam_agırlık < kargo.agırlık12:
            return kargo.fiyat11
        if  kargo.agırlık12 <= toplam_agırlık < kargo.agırlık13:
            return kargo.fiyat12
        if  kargo.agırlık13 <= toplam_agırlık < kargo.agırlık14:
            return kargo.fiyat13
        if  kargo.agırlık14 <= toplam_agırlık :
            return kargo.fiyat14
	
    def get_total_bedel(self):
        return self.get_total_price() + self.get_total_kargo()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
        
    def odeme_bedeli(self):
        kargo = Kargo.objects.first()
        return kargo.bankacılık_bedeli
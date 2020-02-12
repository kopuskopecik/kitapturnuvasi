from django.shortcuts import render, get_object_or_404
from .models import Category, Product, AnaCategory
from cart.forms import CartAddProductForm


def product_list(request):
    categories = AnaCategory.objects.filter(aktif = True).order_by('sıralama_sayısı')
    products1 = Product.objects.filter(category__ana_kategori__aktif = True, category__aktif = True, aktif = True, ogrenci_sayisi = "e").order_by("category__sayi")
    products2 = Product.objects.filter(category__ana_kategori__aktif = True, category__aktif = True, aktif = True, ogrenci_sayisi = "a").order_by("category__sayi")

    ogrenci_sayısı = (
		('b', 10),
		('c', 15),
		('d', 20),
		('e', 25),
		('f', 30),
		('g', 35),
		('h', 40),
		('i', 45),
    )	
	

    context = {
		'ogrenci_sayısı': ogrenci_sayısı,
        'categories': categories,
        'products1': products1,
        'products2': products2,
    }
    return render(request, 'shop/product/list.html', context)

def product_filter_list(request, sayi):
    categories = AnaCategory.objects.filter(aktif = True).order_by('sıralama_sayısı')
    products1 = Product.objects.filter(category__ana_kategori__aktif = True, category__aktif = True, ogrenci_sayisi = sayi, aktif = True).order_by("category__sayi")

    ogrenci_sayısı = (
		('b', 10),
		('c', 15),
		('d', 20),
		('e', 25),
		('f', 30),
		('g', 35),
		('h', 40),
		('i', 45),
    )	


    context = {
		'ogrenci_sayısı': ogrenci_sayısı,
        'categories': categories,
        'products1': products1
    }
    return render(request, 'shop/product/list.html', context)
	
def category_product_list(request, category_slug):
    category = get_object_or_404(AnaCategory, slug=category_slug, aktif = True)
    if not category.bireysel_mi:
        products = Product.objects.filter(category__ana_kategori=category, category__aktif = True, aktif = True,  ogrenci_sayisi = "c").order_by("category__sayi")
    else:
        products = Product.objects.filter(category__ana_kategori=category, category__aktif = True, aktif = True).order_by("category__sayi")
    categories = AnaCategory.objects.exclude(slug = category_slug).filter(aktif = True).order_by('sıralama_sayısı')

    ogrenci_sayısı = (
		('b', 10),
		('c', 15),
		('d', 20),
		('e', 25),
		('f', 30),
		('g', 35),
		('h', 40),
		('i', 45),
    )

    context = {
		'ogrenci_sayısı': ogrenci_sayısı,
        'category': category,
        'products': products,
		'categories': categories
    }
    return render(request, 'shop/product/category_detail.html', context)

def category_product_filter_list(request, category_slug, sayi):
    category = get_object_or_404(AnaCategory, slug=category_slug, aktif = True)
    products = Product.objects.filter(category__ana_kategori=category, ogrenci_sayisi = sayi, aktif = True, category__aktif = True).order_by("category__sayi")
    categories = AnaCategory.objects.exclude(slug = category_slug).filter(aktif =True).order_by('sıralama_sayısı')

    ogrenci_sayısı = (
		('b', 10),
		('c', 15),
		('d', 20),
		('e', 25),
		('f', 30),
		('g', 35),
		('h', 40),
		('i', 45),
    )

    context = {
		'ogrenci_sayısı': ogrenci_sayısı,
        'category': category,
        'products': products,
		'categories': categories
    }
    return render(request, 'shop/product/category_detail.html', context)



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, category__aktif = True, aktif = True)
    products = Product.objects.exclude(ogrenci_sayisi = product.ogrenci_sayisi).filter(category__ana_kategori = product.category.ana_kategori, category = product.category, category__aktif = True, aktif = True).order_by('ogrenci_sayisi')
    print("")
    print(products)
    print("")
    cart_product_form = CartAddProductForm()
    context = {
		'products': products,
        'product': product,
        'form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

def product_detail_nasil_uygulanir(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, category__aktif = True, aktif = True)
    context = {
        'product': product,
    }
    return render(request, 'shop/product/nasil-detail.html', context)

	


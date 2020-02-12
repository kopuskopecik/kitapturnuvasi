from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from shop.models import Product, AnaCategory
from .forms import OrderCreateForm, OrderItemForm, SiparisForm
from cart.cart import Cart
from django.contrib import messages
from django.db.models import Avg, Count, Sum

@login_required
def siparislerim(request):
	siparisler = Order.objects.filter(user = request.user)
	urunler = OrderItem.objects.filter(order__user = request.user)
	print(siparisler)
	context = {
		'siparisler': siparisler,
	}
	
	return render(request, 'orders/order/siparislerim.html', context)


def tum_siparisler(request):
	if not request.user.is_superuser:
		return redirect('/') 
	
	siparisler = Order.objects.all()

	query = request.GET.get("q")
	print(query)
	if query:
		#query = query.replace("I", "ı").replace("İ", "i").lower()
		print(query)
		siparisler = Order.objects.filter(first_name__icontains =query).distinct()
		print(siparisler)

	
	context = {
		'siparisler': siparisler,
	}
	
	return render(request, 'orders/order/siparislerin_hepsi.html', context)

def tum_siparisler_filtre(request, sayi):
	if not request.user.is_superuser:
		return redirect('/') 
	
	
	siparisler = Order.objects.filter(siparis_durumu = sayi)
	context = {
		'siparisler': siparisler,
	}
	
	return render(request, 'orders/order/siparislerin_hepsi.html', context)	

def istatistik (request, gun):
	if not request.user.is_superuser:
		return redirect('/') 
	# bir yıl önceki zamana gidelim
	from datetime import datetime, timedelta
	

	now = datetime.today()
	zaman_farkı = timedelta(gun)
	geçmiş = now - zaman_farkı
	
	küme = set()
	liste = []
	
	küme1 = []
	
	siparisler = Order.objects.all()
	satıs_adedi = siparisler.aggregate(adet = Sum("orderitem__quantity"))
	toplam_satıs = siparisler.aggregate(toplam = Sum("toplam_urun_tutarı"))
	
	siparis_elemanları = OrderItem.objects.filter(order__created__gte = geçmiş)
	urunler = Product.objects.filter(orderitem__order__created__gte = geçmiş)
	urun_sayısı = urunler.annotate(sayi = Sum("orderitem__quantity"))
	kategoriler = AnaCategory.objects.filter(altkategoriler__product__orderitem__order__created__gte = geçmiş)
	kategori_sayısı = kategoriler.annotate(adet = Sum("altkategoriler__product__orderitem__quantity"))
	
		
	
	
	context = {
		'satıs_adedi': satıs_adedi,
		'toplam_satıs': toplam_satıs,
		'gun': gun,
		'siparisler': siparisler,
		'urunler':urunler,
		'urun_sayısı': urun_sayısı,
		'kategori_sayısı': kategori_sayısı,
	}
	
	return render(request, 'orders/order/istatistik.html', context)

def istatistikler (request):
	if not request.user.is_superuser:
		return redirect('/') 
	# bir yıl önceki zamana gidelim
	
	
	
	gunler = {
	
		"bugün": 1, 
		"2 gün": 2, 
		"3 gün": 3, 
		"4 gün": 4,
		"5 gün": 5, 
		"6 gün": 6, 
		'1 hafta': 7,		
		'2 hafta': 14, 
		'3 hafta': 21,
		'1 ay': 30, 
		'2 ay': 60, 
		'3 ay': 90, 
		'4 ay': 120, 
		'5 ay': 150, 
		'6 ay': 180,
		'7 ay': 210,
		'8 ay': 240,
		'9 ay': 270,
		'10 ay': 300,
		'11 ay': 330,
		'1 yıl': 365,
		'2 yıl': 365*2,
		'3 yıl': 365*3,
		'4 yıl': 365*4,
		'5 yıl': 365*5,
		'6 yıl': 365*6,
		'7 yıl': 365*7,
		'8 yıl': 365*8,
		'9 yıl': 365*9,
		'10 yıl': 365*10,
	}
	
	
	
	
	context = {
		'gunler': gunler,
	}
	
	return render(request, 'orders/order/istatistikler.html', context)

def tarih(request):
	if not request.user.is_superuser:
		return redirect('/') 
	
	if request.method=="POST":
		ilk_tarih = request.POST.get("bir")
		ikinci_tarih = request.POST.get("iki")
		
		siparisler = Order.objects.filter(created__date__gte = ilk_tarih, created__date__lte = ikinci_tarih)
		print("")
		print("")
		print(siparisler)
		print("")
		print("")
		satıs_adedi = siparisler.aggregate(adet = Sum("orderitem__quantity"))
		toplam_satıs = siparisler.aggregate(toplam = Sum("toplam_urun_tutarı"))
	
		siparis_elemanları = OrderItem.objects.filter(order__created__date__gte = ilk_tarih, order__created__date__lte = ikinci_tarih)
		urunler = Product.objects.filter(orderitem__order__created__date__gte = ilk_tarih, orderitem__order__created__date__lte = ikinci_tarih)
		urun_sayısı = urunler.annotate(sayi = Sum("orderitem__quantity"))
		kategoriler = AnaCategory.objects.filter(altkategoriler__product__orderitem__order__created__date__gte = ilk_tarih, altkategoriler__product__orderitem__order__created__date__lte = ikinci_tarih)
		kategori_sayısı = kategoriler.annotate(adet = Sum("altkategoriler__product__orderitem__quantity"))
	
		
		context = {
			'satıs_adedi': satıs_adedi,
			'toplam_satıs': toplam_satıs,
			'ilk_tarih': ilk_tarih,
			'ikinci_tarih': ikinci_tarih,
			'siparisler': siparisler,
			'urunler':urunler,
			'urun_sayısı': urun_sayısı,
			'kategori_sayısı': kategori_sayısı,
		}
	
		return render(request, 'orders/order/tarih.html', context)
		#return redirect('anasayfa:anasayfa')
	
	return redirect('anasayfa:anasayfa')
	

def siparis_detail(request, id):
	if not request.user.is_superuser:
		return redirect('/')
	
	siparisler = Order.objects.all()
	siparis = get_object_or_404(Order, id = id)
	
	context = {
		'siparisler': siparisler,
		'siparis': siparis,		
	}
	
	if not siparis == Order.objects.last():
		onceki_siparis = siparis.get_previous_by_created()
		context["onceki_siparis"] = onceki_siparis
	if not siparis == Order.objects.first():
		sonraki_siparis = siparis.get_next_by_created()
		context["sonraki_siparis"] = sonraki_siparis	
	
	return render(request, 'orders/order/siparis-detail.html', context)

def siparis_detail_urun_ekle(request, id):
	if not request.user.is_superuser:
		return redirect('/')
	
	siparis = get_object_or_404(Order, id = id)
	
	form = OrderItemForm(request.POST or None)
	if form.is_valid():
		urun=form.save(commit = False)
		urun.order = siparis
		urun.save()
		messages.success(request, "Ürün başarılı bir şekilde eklendi")
		return HttpResponseRedirect(urun.order.get_absolute_url())
	
	context = {
		"siparis": siparis,
		"form": form,
	}
	
	return render(request, 'orders/order/siparis-detail-urun-ekle.html', context)

def load_cities(request):
    if not request.user.is_superuser:
        return redirect('/')
    country_id = request.GET.get('kategori')
    print("")
    print("")
    print("Kategori Id:", country_id)
    print("")
    print("")
    cities = Product.objects.filter(category__ana_kategori_id=country_id)
    return render(request, 'orders/order/city_dropdown_list_options.html', {'cities': cities})

def siparis_ekle(request):
	if not request.user.is_superuser:
		return redirect('/')
		
	
	form = SiparisForm(request.POST or None)
	if form.is_valid():
		form=form.save()		
		messages.success(request, "Ürün başarılı bir şekilde değiştirildi")
		return HttpResponseRedirect(form.get_absolute_url())
	
	context = {
		"form": form,
	}
	
	return render(request, 'orders/order/siparis-ekle.html', context)

def siparis_duzenle(request, id):
	if not request.user.is_superuser:
		return redirect('/')
	
	siparis = get_object_or_404(Order, id = id)
	form = SiparisForm(request.POST or None, instance = siparis)
	if form.is_valid():
		form=form.save()		
		messages.success(request, "Ürün başarılı bir şekilde eklendi")
		return HttpResponseRedirect(form.get_absolute_url())
	
	context = {
		"form": form,
	}
	
	return render(request, 'orders/order/siparis-ekle.html', context)
	

def order_create(request):
    cart = Cart(request)
    if cart:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save(commit = False)
                if request.user.is_authenticated:
                        order.user = request.user
                order.save()
                print(order)
                for item in cart:
                    print("")
                    print(item)
                    a = OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity'],
                        agırlık = item['agırlık']
                        )
                    print(a)
                cart.clear()
                return render(request, 'orders/order/created.html', {'order': order})
        else:
            form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'form': form})
    else:
        return redirect("anasayfa:anasayfa")
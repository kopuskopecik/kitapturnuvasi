from django.contrib import admin
from .models import Category, Product, Resim, AnaCategory, TekliResim

class ProductInline(admin.StackedInline):
	model = Product

	
class AnaCategoryAdmin(admin.ModelAdmin):
		
	list_display = ['name', 'slug','sayfa_durumu', 'bireysel_mi','sadece_madalyalı_mı', 'sıralama_sayısı', 'aktif', ]
	list_editable = ['slug','sayfa_durumu', 'bireysel_mi','sadece_madalyalı_mı', 'sıralama_sayısı', 'aktif',]
	list_filter = ['name', ]
	prepopulated_fields = {'slug': ('name',)}

	
class CategoryAdmin(admin.ModelAdmin):
		
	list_display = ['name', 'ana_kategori', 'sayi', 'image1', 'nasıl_uygulanır_resimleri', 'odul_buttonu_resimleri', 'madalyalı_mı', 'sayfa_sayısı','aktif']
	list_editable = ['ana_kategori', 'sayi', 'image1', 'nasıl_uygulanır_resimleri', 'odul_buttonu_resimleri', 'madalyalı_mı', 'sayfa_sayısı','aktif']
	prepopulated_fields = {'slug': ('name',)}
	list_filter = ['ana_kategori', 'aktif']
	
	fields = (
		'ana_kategori',
		('name', 'slug'),
		('image1', 'image2', 'nasıl_uygulanır_resimleri'),
		('sayi', 'madalyalı_mı', 'sayfa_sayısı', 'aktif'),
	)


class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'category', 'anasayfada_gosterilsin_mi', 'sıralama_sayısı', 'price', 'agırlık', 'ogrenci_sayisi','aktif']
	list_editable = ['category', 'anasayfada_gosterilsin_mi', 'sıralama_sayısı','price', 'agırlık', 'ogrenci_sayisi', 'aktif']
	list_filter = ['category', 'category__ana_kategori', 'sıralama_sayısı','anasayfada_gosterilsin_mi', 'aktif']
	prepopulated_fields = {'slug': ('name',)}
	
	fields = (
		'category',
		('name', 'slug'),
		'description',
		('price', 'degisiklik', 'agırlık'),
		('ogrenci_sayisi', 'anasayfada_gosterilsin_mi', 'aktif', 'sıralama_sayısı'),
	)


class ResimAdmin(admin.ModelAdmin):
    list_display = ['isim', 'sıralama_sayısı']
    list_editable = ['sıralama_sayısı', ]
    list_filter = ['isim',]
	
    #readonly_fields = ('tekresimler',)

    #def images(self, obj):
    #    from django.utils.html import format_html
    #    html = '<a href="{url}" target="_blank"><img src="{url}" width = "100vw" /></a>'
     #   return format_html(''.join(html.format(url=image.image1.url) for image in obj.resimler.all()))
		
    #def tekresimler(self, obj):
     #   from django.utils.html import format_html
      #  resimler = TekliResim.objects.all()
       # html = '<a href="{url}" target="_blank">{isim}<img src="{url}" width = "100vw" /></a>'
        #return format_html(''.join(html.format(url=image.image1.url, isim = image.isim) for image in resimler))

class TekliResimAdmin(admin.ModelAdmin):
    list_display = ['isim', 'image1', ]
    list_editable = ['image1', ]
    list_filter = ['isim',]

admin.site.register(AnaCategory, AnaCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(TekliResim, TekliResimAdmin)
admin.site.register(Resim, ResimAdmin)



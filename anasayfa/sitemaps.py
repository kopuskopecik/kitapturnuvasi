from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from shop.models import AnaCategory, Product
from .models import Genel, Dokuman

class AnaCategorySitemap(Sitemap):
	protocol = "https"

	def items(self):
		return AnaCategory.objects.filter(aktif = True)


class ProductSitemap(Sitemap):
	protocol = "https"

	def items(self):
		return Product.objects.filter(category__aktif = True, aktif = True)

class GenelSitemap(Sitemap):
	protocol = "https"

	def items(self):
		return Genel.objects.filter(aktif = True)



class StaticViewSitemap(Sitemap):
	protocol = "https"
	
	def items(self):
		return ['anasayfa:ziyaret', 'anasayfa:copyright', 'anasayfa:iletisim', 'anasayfa:dokumanlar',]
	
	def location(self, item):
		return reverse(item)
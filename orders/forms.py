from django import forms
from .models import Order, OrderItem

from shop.models import Product, AnaCategory


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['kargo_tipi','first_name', 'last_name', 'phone', 'email', 'address', 'city', 'siparis_notu']


class OrderItemForm(forms.ModelForm):
	kategori = forms.ModelChoiceField(queryset=AnaCategory.objects.all())
	
	class Meta:
		model = OrderItem
		fields = ['kategori','product', 'quantity']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['product'].queryset = Product.objects.none()
	
		if 'kategori' in self.data:
			try:
				country_id = int(self.data.get('kategori'))
				self.fields['product'].queryset = Product.objects.filter(category__ana_kategori_id=country_id)
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['product'].queryset = self.instance.kategori.category_set.product_set

class SiparisForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['kargo_tipi','first_name', 'last_name', 'phone', 'email', 'address', 'city', 'siparis_notu', "siparis_durumu", "indirim_tutari", "user"]
		
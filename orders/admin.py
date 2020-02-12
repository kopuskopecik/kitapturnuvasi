from django.contrib import admin
from .models import Order, OrderItem
from django.utils.safestring import mark_safe


class OrderInline(admin.TabularInline):
    model = OrderItem
    list_display = ['order', 'product', 'price', 'quantity']
    readonly_fields = ('urun_aciklamasi', )
	
    def urun_aciklamasi(self, obj):
        return mark_safe(obj.product.description)
		

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline,]
    list_display = ['first_name', 'last_name', 'city', 'paid', 'created', 'siparis_durumu', 'siparis_notu', 'indirim_tutari', 'get_total_cost', 'get_total_kargo', 'banka_bedel','get_total_bedel', 'get_indirimli_bedel', ]
    list_filter = ['paid', 'created', 'updated']
    list_editable = ['siparis_durumu', 'paid', 'indirim_tutari',]
    readonly_fields = ('get_total_bedel', 'get_indirimli_bedel',)


admin.site.register(Order, OrderAdmin)


from django.contrib import admin
from .models import Kargo
# Register your models here.

class KargoAdmin(admin.ModelAdmin):
	
	list_display = ('bankacılık_bedeli','agırlık1', 'fiyat1','agırlık2','fiyat2', 
	'agırlık3', 'fiyat3', 'agırlık4', 'fiyat4',
	'agırlık5', 'fiyat5','agırlık6', 'fiyat6','agırlık7', 'fiyat7',
	'agırlık8', 'fiyat8','agırlık9', 'fiyat9','agırlık10', 'fiyat10',
	'agırlık11', 'fiyat11','agırlık12', 'fiyat12','agırlık13', 'fiyat13',
	'agırlık14', 'fiyat14',)
	
	
	list_editable = ('agırlık1', 'fiyat1','agırlık2','fiyat2', 
	'agırlık3', 'fiyat3', 'agırlık4', 'fiyat4',
	'agırlık5', 'fiyat5','agırlık6', 'fiyat6','agırlık7', 'fiyat7',
	'agırlık8', 'fiyat8','agırlık9', 'fiyat9','agırlık10', 'fiyat10',
	'agırlık11', 'fiyat11','agırlık12', 'fiyat12','agırlık13', 'fiyat13',
	'agırlık14', 'fiyat14',)
	

	fields = ('agırlık1', 'fiyat1','agırlık2','fiyat2', 
	'agırlık3', 'fiyat3', 'agırlık4', 'fiyat4',
	'agırlık5', 'fiyat5','agırlık6', 'fiyat6','agırlık7', 'fiyat7',
	'agırlık8', 'fiyat8','agırlık9', 'fiyat9','agırlık10', 'fiyat10',
	'agırlık11', 'fiyat11','agırlık12', 'fiyat12','agırlık13', 'fiyat13',
	'agırlık14', 'fiyat14','bankacılık_bedeli',)
	

admin.site.register(Kargo, KargoAdmin)


from django.db import models
from accounts.models import User

from ckeditor.fields import RichTextField

# Create your models here.
class Entry(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "süperkullanıcı", blank = True, null = True)
	mesaj = RichTextField()
	resim = models.ImageField(blank=True, null = True)
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
	
	class Meta:
		ordering = ["-publishing_date"]
	
	def __str__(self):
		return self.user.username
		
	def get_delete_url(self):
		return reverse('mesaj:mesaj-delete', kwargs={'id':self.id})
		
	

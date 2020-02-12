from django import forms
from .models import Entry

class MesajForm(forms.ModelForm):
	
	class Meta:
		model = Entry
		fields = [
			'mesaj',
			'resim',
			]
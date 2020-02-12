from django.shortcuts import render, Http404, redirect, get_object_or_404
from django.contrib import messages

from .models import Entry
from .forms import MesajForm

# Create your views here.
def mesajlar(request):
	if not request.user.is_superuser:
		return Http404
	
	iletiler = Entry.objects.all() 
		
	context = {
		'iletiler': iletiler,
	}
	
	return render(request, 'mesaj/iletiler.html', context)


def create(request):
	if not request.user.is_superuser:
		return Http404()
	son_mesaj	= Entry.objects.all().first()
	
	form = MesajForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		mesaj=form.save(commit = False)
		mesaj.user = request.user
		mesaj.save()
		messages.success(request, "Mesajınız Başarılı Bir Şekilde Oluşturuldu.",extra_tags="mesaj-basarili")
		return redirect("mesaj:mesajlar")
	
	context = {
		'form':form,
		'son_mesaj': son_mesaj,
	}

	return render(request, 'mesaj/form.html',context)


def update(request, id):
	if not request.user.is_superuser:
		return Http404()
	
	mesaj = get_object_or_404(Entry, id=id)
	if not mesaj == Entry.objects.first(): 
		son_mesaj	= mesaj.get_previous_by_publishing_date()
	else:
		son_mesaj	= Entry.objects.all().first()
	
	form = MesajForm(request.POST or None, request.FILES or None, instance = mesaj)
	if form.is_valid():
		mesaj=form.save(commit = False)
		mesaj.user = request.user
		mesaj.save()
		messages.success(request, "Mesajınız Başarılı Bir Şekilde Değiştirildi.",extra_tags="mesaj-basarili")
		return redirect("mesaj:mesajlar")
	
	context = {
		'form':form,
		'son_mesaj': son_mesaj,
	}

	return render(request, 'mesaj/form.html',context)

def sil(request, id):
	if not request.user.is_superuser:
		return Http404()
	
	mesaj = get_object_or_404(Entry, id=id)
	mesaj.delete()
	return redirect("mesaj:mesajlar")
	
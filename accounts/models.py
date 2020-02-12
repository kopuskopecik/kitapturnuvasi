from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse

#STATUS_CHOICES = (
    #('t', 'Turuncu'),
   # ('m', 'Mavi'),
    #('k', 'Kırmızı'),
	#('s', 'Sarı'),
	#('y', 'Yeşil'),
#)

#ETKINLIK_CHOICES = (
	#('k', 'Kitap Okuma Turnuvası'),
    #('p', 'Kitap Okuma Etkinlikleri'),
    #('a', 'Anlamayı Geliştirme Turnuvası'),
    #('b', 'Birinci Sınıf Okuma Etkinliği'),
	#('o', 'Okul Öncesi Masal Etkinliği'),
	#('l', 'Lise "Kitap Koçum" Etkinliği'),
#)

#ODUL_CHOICES = (
	#('b', 'Birinci Ödül'),
    #('i', 'İkinci Ödül'),
    #('ü', 'Üçüncü Ödül'),
    #('d', 'Dördüncü Ödül'),
#)

class User(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)


	
class Teacher(models.Model):
	teacher = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	okul_adi = models.CharField(max_length= 100, blank = True)
	
	def __str__(self):
		return self.teacher.username
	
	#def etkinlik_olustura_git(self):
	#	return reverse('turnuva:etkinlik_olustur', kwargs={'teacher_id':self.pk})
	
	#def etkinliklerim(self):
	#	return reverse('turnuva:etkinliklerim', kwargs={'teacher_id':self.pk})
		

#class Kitap(models.Model):
#	isim = models.CharField(max_length= 30, blank = True)
#	sayfa = models.PositiveIntegerField()

class Student(models.Model):
	student = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	#kitap = models.ManyToManyField(Kitap, related_name='kitaplar', blank = True)
	#takim = models.CharField(max_length=1, choices=STATUS_CHOICES, blank = True)
	#bireysel_odulu = models.CharField(max_length= 30, blank = True)
	#takim_odulu	= models.CharField(max_length= 30, blank = True)
	ogretmen = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank = True, null = True)
	#sayfa = models.PositiveIntegerField(default = 0)
	#no = models.PositiveIntegerField(default = 0)
	
	def __str__(self):
		return self.student.username
	
	#def kitap_ekle(self):
		#pass
#class Etkinlik(models.Model):
	#isim = models.CharField(max_length=1, choices=ETKINLIK_CHOICES)
	#ogretmen = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank = True, null = True)
	#sinif_adi = models.CharField(max_length= 30)
	#asistan = models.ManyToManyField(Student, related_name='asistanlar')
	#ogrenci = models.ManyToManyField(Student, related_name='ogrenciler')
	#hedef = models.PositiveIntegerField()
	#startting_date = models.DateTimeField(max_length= 30, auto_now_add=True)
	#finishing_date = models.DateTimeField(max_length= 30, auto_now=True)
	#odul = models.CharField(max_length=1, choices=ODUL_CHOICES, blank = True)
	#def __str__(self):
		#return self.sinif_adi + " " + self.get_isim_display() + " " + self.ogretmen.teacher.username
	
	#def get_absolute_url(self):
		#return reverse('turnuva:etkinlik-detail', kwargs={'teacher_id':self.ogretmen.pk, 'etkinlik_id':self.pk})
	 


	
	

		

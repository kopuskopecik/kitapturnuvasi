from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from shop.models import Resim

FONT_RENKLERİ = (

("text-primary", "mavi"),
("text-secondary", "gri"),
("text-success", "yeşil"),
("text-danger", "kırmızı"),
("text-warning", "turuncu"),
("text-info", "açık mavi"),
("text-light", "ince beyaz"),
("text-dark", "koyu siyah"),
("text-body", "az koyu siyah"),
("text-muted", "sönük gri"),
("text-white", "kalın beyaz"),
("text-black-50", "ince siyah"),
("text-white-50", "kalın gri"),

)

OKULLAR = (

    ("İlkokul", "İlkokul"),
    ("Ortaokul", "Ortaokul"),
)

ARKA_PLAN_RENKLERİ = (

	("bg-primary", "mavi"),
	("bg-secondary", "gri"),
	("bg-success", "yeşil"),
	("bg-danger", "kırmızı"),
	("bg-warning", "turuncu"),
	("bg-info", "açık mavi"),
	("bg-light", "ince beyaz"),
	("bg-dark", "koyu siyah"),
	("bg-white", "kalın beyaz"),
	("bg-transparent", "ince siyah"),

)

BUTTON_RENKLERİ = (

	("btn-primary", "mavi"),
	("btn-secondary", "gri"),
	("btn-success", "yeşil"),
	("btn-danger", "kırmızı"),
	("btn-warning", "turuncu"),
	("btn-info", "açık mavi"),
	("btn-light", "ince beyaz"),
	("btn-dark", "koyu siyah"),
	("btn-white", "kalın beyaz"),
	("btn-link", "sadece mavi link"),

)

FONT_SIZE = (
	("8", 8),
	("10", 10),
    ("12", 12),
    ("14", 14),
    ("16", 16),
	("18", 18),
	("20", 20),
	("22", 22),
	("24", 24),
)

class Genel(models.Model):
	başlık = models.CharField(max_length= 100)
	slug = models.SlugField(unique=True, max_length=130)
	resim_grubu = models.ForeignKey(Resim, on_delete=models.CASCADE, blank = True , null = True, verbose_name = "Resim grubu", related_name= "resim_grubu")
	kısa_içerik = RichTextField()
	uzun_içerik = RichTextField()
	aktif = models.BooleanField("aktif mi", default = False)
	sira = models.PositiveIntegerField("Sıralama Sayısı", default = 0)
	
	class Meta:
		verbose_name = 'Genel-Konu'
		verbose_name_plural = 'Genel-Konular'
		ordering = ['sira']
	
	def __str__(self):
		return self.başlık
	
	def get_absolute_url(self):
		return reverse('anasayfa:genel-detail', kwargs={'slug':self.slug})

        
class Slayt(models.Model):
    isim = models.CharField("Başlık", max_length= 50, blank=True)
    yazı = models.CharField("Yazı", max_length= 200, blank=True)
    image = models.ImageField("Dikdörtgen Resim", blank=True, null = True)
    image2 = models.ImageField("Kare Resim", blank=True, null = True)
    aktif = models.BooleanField("Aktif mi?", help_text="Sitede görünmesini istiyorsanız işaretleyiniz!!!", default = False)
    sıralama_sayısı = models.PositiveIntegerField("Anasayfa Sıralama Sayısı", default = 0)

    def __str__(self):
        return self.isim

    class Meta:
        verbose_name = 'Slayt-Resmi'
        verbose_name_plural = 'Slayt-Resimleri'
        ordering = ['sıralama_sayısı']

class Yorum(models.Model):
    isim = models.CharField("Kullanıcı Adı:", max_length= 50)
    okul = models.CharField('Okulunuz:', max_length=30, choices= OKULLAR)
    content = models.TextField("Yorum:")
    aktif = models.BooleanField("Aktif mi?", help_text="Sitede görünmesini istiyorsanız işaretleyiniz!!!", default = False)
    created_at = models.DateTimeField("Oluşturulma tarihi", auto_now_add=True)
    
    class Meta:
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'
        ordering = ['-created_at',]

    def __str__(self):
        return self.isim
    
    def get_absolute_url(self):
        return reverse('anasayfa:ziyaret')

class Dokuman(models.Model):
    isim = models.CharField("Doküman Adı:", max_length= 50)
    slug = models.SlugField(unique=True, max_length=130)
    dokuman_ekle = models.FileField("doküman yükle")
    aktif = models.BooleanField("aktif mi", default = False)
    sira = models.PositiveIntegerField("Sıralama Sayısı", default = 0)
    
    class Meta:
        verbose_name = 'Doküman'
        verbose_name_plural = 'Dokümanlar'

    def __str__(self):
        return self.isim

    def get_absolute_url(self):
        return reverse('anasayfa:dokuman-detail', kwargs={'slug':self.slug})
    

	

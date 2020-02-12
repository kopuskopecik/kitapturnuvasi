from django.db import models

# Create your models here.
class Kargo(models.Model):
    agırlık1 = models.PositiveIntegerField(default=0)
    agırlık2 = models.PositiveIntegerField(default=1)
    agırlık3 = models.PositiveIntegerField(default=5)
    agırlık4 = models.PositiveIntegerField(default=10)
    agırlık5 = models.PositiveIntegerField(default=20)
    agırlık6 = models.PositiveIntegerField(default=30)
    agırlık7 = models.PositiveIntegerField(default=50)
    agırlık8 = models.PositiveIntegerField(default=70)
    agırlık9 = models.PositiveIntegerField(default=85)
    agırlık10 = models.PositiveIntegerField(default=100)
    agırlık11 = models.PositiveIntegerField(default=125)
    agırlık12 = models.PositiveIntegerField(default=150)
    agırlık13 = models.PositiveIntegerField(default=175)
    agırlık14 = models.PositiveIntegerField(default=200)
    fiyat1 = models.PositiveIntegerField(default=6)
    fiyat2 = models.PositiveIntegerField(default=8)
    fiyat3 = models.PositiveIntegerField(default=10)
    fiyat4 = models.PositiveIntegerField(default=15)
    fiyat5 = models.PositiveIntegerField(default=20)
    fiyat6 = models.PositiveIntegerField(default=30)
    fiyat7 = models.PositiveIntegerField(default=50)
    fiyat8 = models.PositiveIntegerField(default=60)
    fiyat9 = models.PositiveIntegerField(default=70)
    fiyat10 = models.PositiveIntegerField(default=80)
    fiyat11 = models.PositiveIntegerField(default=100)
    fiyat12 = models.PositiveIntegerField(default=150)
    fiyat13 = models.PositiveIntegerField(default=200)
    fiyat14 = models.PositiveIntegerField(default=250)
    bankacılık_bedeli = models.PositiveIntegerField(default=7)
    
    class Meta:
        verbose_name = 'Kargo-Ağırlık Değeri'
        verbose_name_plural = 'Kargo-Ağırlık Değeri'

    def __str__(self):
        return "kargo ağırlık aralıkları"
# Generated by Django 2.0 on 2020-02-12 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kargo_tipi', models.CharField(choices=[('1', 'Kapıda Nakit Ödeme'), ('2', 'Kapıda Tek Çekim Kredi Kartı Ödeme'), ('3', 'Havale/EFT')], help_text='Blabla', max_length=10, verbose_name='Ödeme Tercihiniz:')),
                ('first_name', models.CharField(max_length=60, verbose_name='Adınız:')),
                ('last_name', models.CharField(max_length=60, verbose_name='Soyadınız:')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(verbose_name='Adres:')),
                ('phone', models.CharField(blank=True, help_text='İrtibat Numarası', max_length=20, verbose_name='Telefon No:')),
                ('city', models.CharField(choices=[['1', 'Adana'], ['2', 'Adıyaman'], ['3', 'Afyonkarahisar'], ['4', 'Ağrı'], ['5', 'Aksaray'], ['6', 'Amasya'], ['7', 'Ankara'], ['8', 'Antalya'], ['9', 'Ardahan'], ['10', 'Artvin'], ['11', 'Aydın'], ['12', 'Balıkesir'], ['13', 'Bartın'], ['14', 'Batman'], ['15', 'Bayburt'], ['16', 'Bilecik'], ['17', 'Bingöl'], ['18', 'Bitlis'], ['19', 'Bolu'], ['20', 'Burdur'], ['21', 'Bursa'], ['22', 'Çanakkale'], ['23', 'Çankırı'], ['24', 'Çorum'], ['25', 'Denizli'], ['26', 'Diyarbakır'], ['27', 'Düzce'], ['28', 'Edirne'], ['29', 'Elazığ'], ['30', 'Erzincan'], ['31', 'Erzurum'], ['32', 'Eskişehir'], ['33', 'Gaziantep'], ['34', 'Giresun'], ['35', 'Gümüşhane'], ['36', 'Hakkâri'], ['37', 'Hatay'], ['38', 'Iğdır'], ['39', 'Isparta'], ['40', 'İstanbul'], ['41', 'İzmir'], ['42', 'Kahramanmaraş'], ['43', 'Karabük'], ['44', 'Karaman'], ['45', 'Kars'], ['46', 'Kastamonu'], ['47', 'Kayseri'], ['48', 'Kilis'], ['49', 'Kırıkkale'], ['50', 'Kırklareli'], ['51', 'Kırşehir'], ['52', 'Kocaeli'], ['53', 'Konya'], ['54', 'Kütahya'], ['55', 'Malatya'], ['56', 'Manisa'], ['57', 'Mardin'], ['58', 'Mersin'], ['59', 'Muğla'], ['60', 'Muş'], ['61', 'Nevşehir'], ['62', 'Niğde'], ['63', 'Ordu'], ['64', 'Osmaniye'], ['65', 'Rize'], ['66', 'Sakarya'], ['67', 'Samsun'], ['68', 'Şanlıurfa'], ['69', 'Siirt'], ['70', 'Sinop'], ['71', 'Sivas'], ['72', 'Şırnak'], ['73', 'Tekirdağ'], ['74', 'Tokat'], ['75', 'Trabzon'], ['76', 'Tunceli'], ['77', 'Uşak'], ['78', 'Van'], ['79', 'Yalova'], ['80', 'Yozgat'], ['81', 'Zonguldak']], max_length=10, verbose_name='Şehir:')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False, verbose_name='Ödenme durumu')),
                ('siparis_durumu', models.CharField(choices=[('1', 'İşlemde'), ('2', 'Hazırlanıyor'), ('3', 'Kargoya Teslim Edildi'), ('4', 'İptal')], default='1', max_length=10, verbose_name='Sipariş Durumu:')),
                ('siparis_notu', models.TextField(blank=True, verbose_name='Sipariş Notu:')),
                ('indirim_tutari', models.PositiveIntegerField(default=0, verbose_name='İndirim Miktarı')),
                ('toplam_urun_tutarı', models.PositiveIntegerField(default=0, verbose_name='Ürün bedeli')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Müşteri')),
            ],
            options={
                'verbose_name': 'Sipariş',
                'verbose_name_plural': 'Siparişler',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Fiyat')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Miktar')),
                ('agırlık', models.FloatField(default=0, verbose_name='Ağırlık')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Sipariş')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='Ürün')),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
            },
        ),
    ]
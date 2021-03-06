# Generated by Django 2.0 on 2020-02-12 19:21

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnaCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='kategori adı')),
                ('slug', models.SlugField(help_text='Burası yalnızca site-dizaynı için. Dokunmayınız!', max_length=150, unique=True, verbose_name='internet adresi')),
                ('sayfa_durumu', models.BooleanField(default=False, help_text='1500-2500 gibi sayfa sayısı varsa işaretlenecek', verbose_name='Sayfa Sayısı Var mı?')),
                ('bireysel_mi', models.BooleanField(default=False, help_text='Öğrencilerle beraber oynanMAyacaksa işaretlenecek!!!', verbose_name='Bireysel mi')),
                ('sadece_madalyalı_mı', models.BooleanField(default=False, help_text='Herhangi bir oyun olmaksızın bir kategori ise işaretlenecek Örneğin; sadece madalya için', verbose_name='Sadece Madalya mı')),
                ('sıralama_sayısı', models.PositiveIntegerField(verbose_name='Sıralama Sayısı')),
                ('aktif', models.BooleanField(default=False, help_text='Sitede görünmesini istiyorsanız işaretleyiniz!!!', verbose_name='Aktif mi?')),
                ('indirim_miktarı', models.PositiveIntegerField(default=0, verbose_name='İndirim miktarı')),
                ('arka_plan_renk', models.CharField(choices=[('btn-primary', 'mavi'), ('btn-secondary', 'gri'), ('btn-success', 'yeşil'), ('btn-danger', 'kırmızı'), ('btn-warning', 'turuncu'), ('btn-info', 'açık mavi'), ('btn-light', 'ince beyaz'), ('btn-dark', 'koyu siyah'), ('btn-white', 'kalın beyaz'), ('btn-link', 'sadece mavi link')], default='btn-primary', max_length=50, verbose_name='Anakategori arka plan rengi')),
            ],
            options={
                'verbose_name': 'Ana-Kategori',
                'verbose_name_plural': 'Ana-Kategoriler',
                'ordering': ('sıralama_sayısı',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='kategori adı')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='internet adresi')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Küçültülmüş Kategori Resmi')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Gerçek Kategori Resmi')),
                ('sayi', models.PositiveIntegerField(verbose_name='Sıralama Sayısı')),
                ('madalyalı_mı', models.BooleanField(default=True, verbose_name='Madalyalı mı')),
                ('sayfa_sayısı', models.CharField(choices=[('a', 0), ('a', 1000), ('b', 1500), ('c', 2500)], max_length=1, verbose_name='sayfa sayısı')),
                ('aktif', models.BooleanField(default=False, help_text='Sitede görünmesini istiyorsanız işaretleyiniz!!!', verbose_name='Aktif mi?')),
                ('ana_kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='altkategoriler', to='shop.AnaCategory', verbose_name='Ana Kategori')),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategoriler',
                'ordering': ('sayi',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='ürün adı')),
                ('slug', models.SlugField(max_length=100, verbose_name='internet adresi')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Ürün açıklaması')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='gerçek fiyat')),
                ('degisiklik', models.IntegerField(default=0, verbose_name='degisiklik')),
                ('agırlık', models.FloatField(default=0, verbose_name='Ağırlık')),
                ('ogrenci_sayisi', models.CharField(choices=[('a', 0), ('b', 10), ('c', 15), ('d', 20), ('e', 25), ('f', 30), ('g', 35), ('h', 40), ('i', 45)], max_length=1)),
                ('anasayfada_gosterilsin_mi', models.BooleanField(default=False, help_text='Anasayfada gösterilmesi istenen ürünler için işaretlenecektir.', verbose_name='AnaSayfada gösterilsin mi?')),
                ('aktif', models.BooleanField(default=False, help_text='Sitede görünmesini istiyorsanız işaretleyiniz!!!', verbose_name='Aktif mi?')),
                ('sıralama_sayısı', models.PositiveIntegerField(default=0, verbose_name='Anasayfa Sıralama Sayısı')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='kategori')),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
                'ordering': ('sıralama_sayısı',),
            },
        ),
        migrations.CreateModel(
            name='Resim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100, verbose_name='resim adı')),
                ('sıralama_sayısı', models.PositiveIntegerField(default=0, verbose_name='Sıralama Sayısı')),
            ],
            options={
                'verbose_name': 'Resim-Grubu',
                'verbose_name_plural': 'Resim-Grupları',
                'ordering': ('sıralama_sayısı', 'isim'),
            },
        ),
        migrations.CreateModel(
            name='TekliResim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100, verbose_name='resim adı')),
                ('image1', models.ImageField(upload_to='', verbose_name='resim')),
            ],
            options={
                'verbose_name': 'Resim',
                'verbose_name_plural': 'Resimler',
                'ordering': ('isim',),
            },
        ),
        migrations.AddField(
            model_name='resim',
            name='resimler',
            field=models.ManyToManyField(blank=True, to='shop.TekliResim', verbose_name='resimler'),
        ),
        migrations.AddField(
            model_name='category',
            name='nasıl_uygulanır_resimleri',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nasil', to='shop.Resim', verbose_name='Nasıl Uygulanır Resimleri'),
        ),
        migrations.AddField(
            model_name='category',
            name='odul_buttonu_resimleri',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='odul', to='shop.Resim', verbose_name='Kişiye özel Ödül Butonu Resimleri'),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]

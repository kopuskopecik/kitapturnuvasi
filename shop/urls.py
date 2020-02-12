from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
	path('<str:sayi>/', views.product_filter_list, name="product_list__filter"),
    url(r'^kategoriler/(?P<category_slug>[-\w]+)/$', views.category_product_list, name='product_list_by_category'),
	path('kategoriler/<slug:category_slug>/<str:sayi>/', views.category_product_filter_list, name="product_list__filter_by_category"),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/nasil-uygulanir/$', views.product_detail_nasil_uygulanir, name='nasil'),
]

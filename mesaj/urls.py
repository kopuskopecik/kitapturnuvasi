from django.urls import path
from . import views

app_name = 'mesaj'

urlpatterns = [
   	path('mesajlar/', views.mesajlar, name='mesajlar'),
	path('mesajlar/create', views.create, name='mesaj-create'),
	#path('mesajlar/<int:id>/', views.detail, name='mesaj-detail'),
	path('mesajlar/<int:id>/update', views.update, name='mesaj-update'),
	path('mesajlar/<int:id>/delete', views.sil, name='mesaj-delete'),
]
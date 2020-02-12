from django.urls import path

from . import views

app_name = 'anasayfa'
urlpatterns = [
    path('', views.AnaSayfa.as_view(), name='anasayfa'),
    path('ziyaretci-defteri/', views.ZiyaretView.as_view(), name='ziyaret'),
    path('yasal-uyarı/', views.YasalView.as_view(), name='copyright'),
    path('dokumanlar/', views.DokumanListView.as_view(), name='dokumanlar'),
    path('iletisim/', views.IletisimView.as_view(), name='iletisim'),
    path('cok-satanlar/', views.cok_satanlar, name='cok_satanlar'),
    #path('deneme/', views.deneme, name='deneme'),
    #path('dokumanlar/<slug:slug>/.docx/', views.DokumanListView.as_view(), name='dokuman-detail'),
    path('genel/<slug:slug>/', views.GenelDetailView.as_view(), name='genel-detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
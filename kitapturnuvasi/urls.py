"""turnuva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from orders.views import load_cities

from accounts.views import TeacherSignUpView, UserUpdateView, SignUpView, UyelikView
from anasayfa.sitemaps import AnaCategorySitemap, ProductSitemap, StaticViewSitemap, GenelSitemap

sitemaps = {
	'kategoriler' : AnaCategorySitemap,
	'urunler': ProductSitemap,
	'statikler': StaticViewSitemap,
	'genel': GenelSitemap,
}

handler404 = 'anasayfa.views.view_404'

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('anasayfa.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    #path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
	#path('accounts/turnuva/', turnuva, name='turnuva'),
	
	path('google102aeaa3d2712612.html', TemplateView.as_view(template_name="google102aeaa3d2712612.html")),
	path('t4qt79m922kcpzkf7tuwn3mmebsdva.html', TemplateView.as_view(template_name="t4qt79m922kcpzkf7tuwn3mmebsdva.html")),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type ="text/plain")),
	path('sitemap.xml/', sitemap, {'sitemaps':sitemaps}),
	
	
	path('uyelik/', UyelikView.as_view(), name = 'uyelik'),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
		
	url(r'^settings/account/$', UserUpdateView.as_view(), name='my_account'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
	
	path('ajax/load-cities/', load_cities, name='ajax_load_cities'),  # <-- this one here
	
	path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('shop/', include('shop.urls')),
	path('mesaj/', include('mesaj.urls')),
	
	
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

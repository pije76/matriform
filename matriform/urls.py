"""matriform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from formapp.views import main, PDFTempview, OrderListJson
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',main,name='main'),
    # url(r'^reg/$',registration,name='reg'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},
        name='matri_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': 'main'}, name='matri_logout'),
    url(r'^pdf/$', PDFTempview, name='pdf'),
    url(r'^my/datatable/data/$', OrderListJson.as_view(), name='order_list_json'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

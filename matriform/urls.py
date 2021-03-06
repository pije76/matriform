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
from formapp.views import (main, PDFTempview, olistjson,molistjson,bolistjson,
    PDF,MatriaspirantDetailView,matriaspirantUpdate,user_create,move_to_married,move_to_bin,
    restore_to_fresh)
from formapp.forms import MyAuthenticationForm
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',main,name='main'),
    # url(r'^reg/$',registration,name='reg'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html', 'authentication_form':MyAuthenticationForm},
        name='matri_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': 'main'}, name='matri_logout'),
    url(r'^pdf/$', PDFTempview, name='pdf'),
    url(r'^pd/$', PDF.as_view(), name='pd'),
    url(r'^create_user/$',(CreateView.as_view(model=User, get_success_url =lambda: reverse('create_user'), form_class=UserCreationForm, template_name="create_user.html")), name='create_user'),
    url(r'^matriaspirant/view/(?P<pk>[0-9]+)/$', MatriaspirantDetailView.as_view(), name='matriaspirant-detail'),
    url(r'matriaspirant/edit/(?P<pk>[0-9]+)/$', matriaspirantUpdate.as_view(), name='matriaspirants_update'),
    url(r'^move/bin/(?P<pk>[0-9]+)/$', move_to_bin, name='move_bin'),
    url(r'^move/married/(?P<pk>[0-9]+)/$', move_to_married, name='move_married'),
    url(r'^restore/fresh/(?P<pk>[0-9]+)/$', restore_to_fresh, name='restore_fresh'),
    url(r'^createuser/$', user_create, name='create_users'),
    url(r'^my/datatable/data/$', olistjson, name='order_list_json'),
    url(r'^my/datatable/mdata/$', molistjson, name='morder_list_json'),
    url(r'^my/datatable/bdata/$', bolistjson, name='border_list_json'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

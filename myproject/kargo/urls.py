"""kargo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from orders import views as orders_views
from orders import urls as orders_url

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),  # admin site

    # front app
    url(r'^$', orders_views.index, name="home"),

    # linked url in module orders from main urls.py to app url
    url(r'^order/', include(orders_url, namespace="order")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

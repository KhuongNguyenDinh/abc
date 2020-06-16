"""baithi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from inside import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'inside/', include('inside.urls')),
    path(r'cart/', include('cart.urls')),
    path(r'social-auth/', include('social_django.urls', namespace="social")),
    path(r'orders/', include('orders.urls')),
    path(r'accounts/', include('allauth.urls')),
    path(r'booking/', include('bookingsite.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

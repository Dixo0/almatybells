"""
URL configuration for almatybells_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from shop import views as shop_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Авторизация
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', shop_views.register, name='register'),

    # КОРЗИНА
    path('cart/', shop_views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', shop_views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', shop_views.cart_remove, name='cart_remove'),
    path('order/create/', shop_views.order_create, name='order_create'),
    path('payment/done/<int:order_id>/', shop_views.payment_process, name='payment_process'),

    # Каталог
    path('', shop_views.product_list, name='product_list'),
    path('<slug:category_slug>/', shop_views.product_list, name='product_list_by_category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

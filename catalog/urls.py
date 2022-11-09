from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('product/<slug:slug>/', ShowProduct.as_view(), name='product'),
    path('category_list/<slug:slug>/', CategoryList.as_view(), name='category_list'),
    path('basket/', my_basket, name='basket'),
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('user_room/', UserRoom.as_view(), name='user_room'),
    path('add_basket/<slug:slug>/', add_basket, name='add_basket'),
    path('remove_basket/<slug:slug>/', remove_basket, name='remove_basket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('login', views.login,name='login'),
    path('sign_up', views.sign_up,name='sign_up'),
    path('logout', views.logout,name='logout'),
    path('home', views.home,name='home'),
    path('makeup',views.makeup,name='makeup'),
    path('skincare',views.skincare,name='skincare'),
    path('purchase', views.purchase,name='purchase'),
    path('about_us',views.about_us,name='about_us'),
    # path('delete_product', views.delete_product, name='delete_product'),
]

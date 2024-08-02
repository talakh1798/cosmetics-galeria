
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('login', views.login,name='login'),
    path('sign_up', views.sign_up,name='sign_up'),
    # path('logout', views.logout,name='logout'),
    path('home', views.home,name='home'),
    path('makeup',views.makeup,name='makeup'),
    path('skincare',views.skincare,name='skincare'),
]

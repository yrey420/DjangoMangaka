

from django.urls import path, include
from personas import views

urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('accounts/', include('allauth.urls')),
    path('reset/', views.reset, name='reset'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register_view, name='register'),
    path('accounts/', include('allauth.urls')),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('forgot-password', views.forgotPassword, name='forgot-password'),
    path('404', views.e404, name='404'),
    path('blank', views.blank, name='blank'),

]
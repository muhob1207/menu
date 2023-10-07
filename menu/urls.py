"""
URL configuration for menu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from menu_app import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', views.HomePage.as_view(), name='home'),

    path('menu1/', views.Menu1.as_view(), name='menu1'),
    path('menu2/', views.Menu2.as_view(), name='menu2'),
    path('menu3/', views.Menu3.as_view(), name='menu3'),

    path('menu1_submenu1/', views.Menu1Submenu1.as_view(), name='menu1_submenu1'),
    path('menu1_submenu2/', views.Menu1Submenu2.as_view(), name='menu1_submenu2'),
    path('menu2_submenu1/', views.Menu2Submenu1.as_view(), name='menu2_submenu1'),
    path('menu2_submenu2/', views.Menu2Submenu2.as_view(), name='menu2_submenu2'),
    path('menu3_submenu1/', views.Menu3Submenu1.as_view(), name='menu3_submenu1'),
    path('menu3_submenu2/', views.Menu3Submenu2.as_view(), name='menu3_submenu2'),

    path('menu1_submenu1_submenu1/', views.Menu1Submenu1Submenu1.as_view(), name='menu1_submenu1_submenu1'),
    path('menu1_submenu1_submenu2/', views.Menu1Submenu1Submenu2.as_view(), name='menu1_submenu1_submenu2'),
    path('menu1_submenu1_submenu3/', views.Menu1Submenu1Submenu3.as_view(), name='menu1_submenu1_submenu3'),
    path('menu1_submenu2_submenu1/', views.Menu1Submenu2Submenu1.as_view(), name='menu1_submenu2_submenu1'),
    path('menu1_submenu2_submenu2/', views.Menu1Submenu2Submenu2.as_view(), name='menu1_submenu2_submenu2'),
    path('menu1_submenu2_submenu3/', views.Menu1Submenu2Submenu3.as_view(), name='menu1_submenu2_submenu3'),
        
    path('menu2_submenu1_submenu1/', views.Menu2Submenu1Submenu1.as_view(), name='menu2_submenu1_submenu1'),
    path('menu2_submenu1_submenu2/', views.Menu2Submenu1Submenu2.as_view(), name='menu2_submenu1_submenu2'),
    path('menu2_submenu1_submenu3/', views.Menu2Submenu1Submenu3.as_view(), name='menu2_submenu1_submenu3'),
    path('menu2_submenu2_submenu1/', views.Menu2Submenu2Submenu1.as_view(), name='menu2_submenu2_submenu1'),
    path('menu2_submenu2_submenu2/', views.Menu2Submenu2Submenu2.as_view(), name='menu2_submenu2_submenu2'),
    path('menu2_submenu2_submenu3/', views.Menu2Submenu2Submenu3.as_view(), name='menu2_submenu2_submenu3'),

    path('menu3_submenu1_submenu1/', views.Menu3Submenu1Submenu1.as_view(), name='menu3_submenu1_submenu1'),
    path('menu3_submenu1_submenu2/', views.Menu3Submenu1Submenu2.as_view(), name='menu3_submenu1_submenu2'),
    path('menu3_submenu1_submenu3/', views.Menu3Submenu1Submenu3.as_view(), name='menu3_submenu1_submenu3'),
    path('menu3_submenu2_submenu1/', views.Menu3Submenu2Submenu1.as_view(), name='menu3_submenu2_submenu1'),
    path('menu3_submenu2_submenu2/', views.Menu3Submenu2Submenu2.as_view(), name='menu3_submenu2_submenu2'),
    path('menu3_submenu2_submenu3/', views.Menu3Submenu2Submenu3.as_view(), name='menu3_submenu2_submenu3'),

    path('menu1_submenu1_submenu1_submenu1/', views.Menu1Submenu1Submenu1Submenu1.as_view(), name='menu1_submenu1_submenu1_submenu1'),

]

"""
URL configuration for plateforme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from tafika import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.importation, name='liste'),
    path('delete/<int:id>/', views.suppression, name='suppression'),
    path('afficher_modifications', views.afficher_modifications, name='afficher_modifications'),
    path('<int:beneficiaire_id>/', views.modifier_beneficiaire, name='modifier_beneficiaire'),
    path('donne_modif', views.afficher_modifications, name='donne_modif'),

    
    
    
]

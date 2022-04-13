from django.urls import path

#from recipes.views import home
from . import views

# . significa algo como 'caminho irmão'. (da pasta que eu estou import views)
views

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipes),
]

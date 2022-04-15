from django.urls import path

#from recipes.views import home
from . import views

# . significa algo como 'caminho irmão'. (da pasta que eu estou import views)
# views

app_name = 'recipes'

urlpatterns = [
    #path('', views.home, name="recipes-home"),
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipes, name="recipe"),
]

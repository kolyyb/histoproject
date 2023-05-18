from django.urls import path
from . import views

app_name = 'qhf'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:card_id>/', views.show_card, name='show_card'),
    path('category_list/', views.category_list, name='category_list'),
]

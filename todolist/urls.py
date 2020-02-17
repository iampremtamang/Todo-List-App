from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('delete/<str:list_id>', views.delete, name = 'delete'),
    path('cross_off/<str:list_id>', views.cross_off, name = "cross_off"),
    path('uncross/<str:list_id>', views.uncross, name = 'uncross'),
    path('edit/<str:list_id>',views.edit, name = 'edit'),

]

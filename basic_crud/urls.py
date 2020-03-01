from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('addnew/', views.add, name='add'),
    path('addnew/<int:id>/', views.add, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

]

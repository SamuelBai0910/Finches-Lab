from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail,name='detail' ),
    path('finches/create/', views.FinchCreate.as_view(),
    name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('habitats/', views.HabitatList.as_view(), name='habitats_index'),
    path('habitats/<int:pk>/', views.HabitatDetail.as_view(), name='habitats_detail'),
    path('habitats/create/', views.HabitatCreate.as_view(), name='habitats_create'),
    path('habitats/<int:pk>/update/', views.HabitatUpdate.as_view(), name='habitats_update'),
    path('habitats/<int:pk>/delete/', views.HabitatDelete.as_view(), name='habitats_delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('create/', views.record_create, name='record_create'),
    path('edit/<int:pk>/', views.record_edit, name='record_edit'),
    path('delete/<int:pk>/', views.record_delete, name='record_delete'),
    path('references/', views.reference_list, name='reference_list'),
    path('references/status/add/', views.status_add, name='status_add'),
    path('references/status/edit/<int:pk>/', views.status_edit, name='status_edit'),
    path('references/status/delete/<int:pk>/', views.status_delete, name='status_delete'),
    path('references/type/add/', views.type_add, name='type_add'),
    path('references/type/edit/<int:pk>/', views.type_edit, name='type_edit'),
    path('references/type/delete/<int:pk>/', views.type_delete, name='type_delete'),
    path('references/category/add/', views.category_add, name='category_add'),
    path('references/category/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('references/category/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('references/subcategory/add/', views.subcategory_add, name='subcategory_add'),
    path('references/subcategory/edit/<int:pk>/', views.subcategory_edit, name='subcategory_edit'),
    path('references/subcategory/delete/<int:pk>/', views.subcategory_delete, name='subcategory_delete'),
]
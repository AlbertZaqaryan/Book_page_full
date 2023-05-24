from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('authors/<int:id>/', views.index_detail, name='index_detail'),
    path('books/<int:id>/', views.index_detail_book, name='index_detail_book'),
    path('contact/', views.contact, name='contact'),
    path('card/', views.card, name='card'),
    path('delete_prod/', views.delete_prod, name='delete_prod'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
]
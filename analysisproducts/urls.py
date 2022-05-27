from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('company/<str:slug>/',views.company_page),
    path('<int:pk>/', views.ProductDetail.as_view()),
]
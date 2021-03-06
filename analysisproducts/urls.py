from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    #path('company/<str:slug>/',views.company_page),
    path('category/<str:slug>/',views.category_page),
    path('<int:pk>/', views.ProductDetail.as_view()),
    path('search/<str:q>/',views.ProductSearch.as_view()),
]
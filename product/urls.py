from django.urls import path, include
from product import views

urlpatterns = [
    path('latest-product/', views.LatestProductsList.as_view())
]
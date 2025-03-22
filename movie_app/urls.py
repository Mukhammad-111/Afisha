from django.urls import path
from . import views


urlpatterns = [
    path('directors/', views.director_list_create_api_view),
    path('directors/<int:id>/', views.director_detail_api_view),
    path('movies/', views.movies_list_create_api_view),
    path('movies/<int:id>/', views.movies_detail_api_view),
    path('movies/reviews/', views.movies_reviews_api_view),
    path('reviews/', views.reviews_list_create_api_view),
    path('reviews/<int:id>/', views.reviews_detail_api_view),
]
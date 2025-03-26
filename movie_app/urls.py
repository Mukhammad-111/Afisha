from django.urls import path
from . import views
from utils.constants import LIST_CREATE, RETRIEVE_UPDATE_DESTROY


urlpatterns = [
    path('directors/', views.DirectorListCreateAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorRetrieveUpdateDestroyAPIView.as_view()),
    path('movies/', views.MovieModelViewSet.as_view(LIST_CREATE)),
    path('movies/<int:id>/', views.MovieModelViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),
    path('movies/reviews/', views.MoviesReviewsListAPIView.as_view()),
    path('reviews/', views.ReviewsModelViewSet.as_view(LIST_CREATE)),
    path('reviews/<int:id>/', views.ReviewsModelViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),
]
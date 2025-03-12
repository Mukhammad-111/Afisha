from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializer import (DirectorSerializer, DirectorDetailSerializer, MovieSerializer,
                         MovieDetailSerializer, ReviewSerializer, ReviewDetailSerializer, MovieReviewSerializer)
from rest_framework import status


@api_view(['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(instance=directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error':'Director not found!'}, status=status.HTTP_404_NOT_FOUND)
    data = DirectorDetailSerializer(director, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movies_list_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error':'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
    data = MovieDetailSerializer(movie, many=False).data
    return Response(data=data)


@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(instance=reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'}, status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movies_reviews_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieReviewSerializer(instance=movies, many=True)
    return Response(data=serializer.data)

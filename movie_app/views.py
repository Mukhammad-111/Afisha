from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializer import (DirectorSerializer, DirectorDetailSerializer, MovieSerializer, MovieDetailSerializer,
                         ReviewSerializer, ReviewDetailSerializer, MovieReviewSerializer)
from rest_framework import status


@api_view(['GET', 'POST'])
def director_list_create_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(instance=directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        # step 1: Receive data from RequestBody
        name = request.data.get('name')

        # step 2: Create director
        director = Director.objects.create(name=name)

        # step 3: return Response(data=director, status=201)
        return Response(data=DirectorDetailSerializer(director).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorDetailSerializer(director, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorDetailSerializer(director).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movies_list_create_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.select_related('director').all()
        serializer = MovieSerializer(instance=movies, many=True)
        return Response(data=serializer.data)
    if request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')

        movie = Movie(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )
        movie.save()

        return Response(data=MovieDetailSerializer(movie).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieDetailSerializer(movie, many=False).data
        return Response(data=data)
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data=MovieDetailSerializer(movie).data, status=status.HTTP_201_CREATED)


@api_view(['GET', "POST"])
def reviews_list_create_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.select_related('movie').all()
        serializer = ReviewSerializer(instance=reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')

        review = Review.objects.create(
            text=text,
            stars=stars,
            movie_id=movie_id
        )

        return Response(data=ReviewDetailSerializer(review).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = ReviewDetailSerializer(review, many=False).data
        return Response(data=data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie_id = request.data.get('movie_id')
        review.save()
        return Response(data=ReviewDetailSerializer(review).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movies_reviews_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieReviewSerializer(instance=movies, many=True)
    return Response(data=serializer.data)

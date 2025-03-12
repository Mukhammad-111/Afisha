from rest_framework import serializers
from . import models


class DirectorSerializer(serializers.ModelSerializer):
    quantity_films = serializers.SerializerMethodField()
    class Meta:
        model = models.Director
        fields = 'id name quantity_films'.split()

    def get_quantity_films(self, director):
        return director.movies.count()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = 'title description duration director'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class MovieReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()
    class Meta:
        model = models.Movie
        fields = 'movie_title director reviews_info average_rating'.split()

    def get_movie_title(self, movie):
        return movie.title if movie else None


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


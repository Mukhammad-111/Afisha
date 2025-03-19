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


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=2, max_length=255)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    duration = serializers.FloatField()
    director_id = serializers.IntegerField(min_value=1)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    stars = serializers.IntegerField(default=4, min_value=1, max_value=5)
    movie_id = serializers.IntegerField(min_value=1)
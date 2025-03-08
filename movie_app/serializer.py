from rest_framework import serializers
from . import models


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = ['id', 'name']


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        exclude = 'duration'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


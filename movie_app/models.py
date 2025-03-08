from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255, default='Akan Sataev')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(blank=True, default="The best")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
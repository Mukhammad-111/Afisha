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

    @property
    def reviews_info(self):
        return [{review.text: review.stars }for review in self.reviews.all()]

    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            grades = [review.stars for review in reviews]
            return sum(grades) / len(grades)
        return 0

STARS = (
    (star, '* ' * star) for star in range(1, 6)
)


class Review(models.Model):
    text = models.TextField(blank=True, default="The best")
    stars = models.IntegerField(choices=STARS, default=4)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text


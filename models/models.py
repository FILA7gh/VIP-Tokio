from django.db import models


class Model(models.Model):
    photo = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    description = models.TextField(default='The real stallion 💪')
    height = models.FloatField(default=180)
    weight = models.FloatField(default=70)
    is_virgin = models.BooleanField(default=False)
    price = models.FloatField(default=1000)

    def __str__(self):
        return self.name

    @property
    def rating(self):
        all_stars = [review.stars for review in self.reviews.all()]
        return round(sum(all_stars) / len(all_stars), 2) if len(all_stars) > 0 else 0


class Review(models.Model):
    CHOICE = ((i, '*' * i) for i in range(1, 6))
    stars = models.IntegerField(choices=CHOICE)
    text = models.CharField()
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.model.name

    @property
    def model_name(self):
        return self.model.name

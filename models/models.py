from django.db import models


class Model(models.Model):
    photo = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=50, default=20)
    description = models.TextField(default='The real stallion 💪')
    height = models.FloatField(default=180)
    weight = models.FloatField(default=70)
    is_virgin = models.BooleanField(default=False)
    price = models.FloatField(default=1000)

    def __str__(self):
        return self.name

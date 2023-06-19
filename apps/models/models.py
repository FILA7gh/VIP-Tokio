from apps.services.models import *
from django.db import models


class Model(models.Model):
    CHOICE_APPEARANCE = (('Азиатская', 'aзиатская'), ('Европейская', 'европейская'), ('Экзотика', 'экзотика'))
    CHOICE_EYES = (('Карие', 'карие'), ('Черные', 'черные'), ('Зеленые', 'зеленые'),
                   ('Голубые', 'голубые'), ('Серые', 'серые'))
    CHOICE_HAIRS = (('Брюнетка', 'брюнетка'), ('Блондинка', 'блондинка'),
                    ('Шатенка', 'шатенка'), ('Рыжие', 'рыжие'), ('Мелированные', 'мелированные'))
    CHOICE_TYPE = (('Индивидуалка', 'индивидуалка'), ('Салон', 'салон'))
    CHOICE_BREAST = (('0-1', '0-1'), ('1', '1'), ('1.5', '1.5'),
                     ('2', '2'), ('2.5', '2.5'), ('3', '3'),
                     ('3.5', '3.5'), ('4', '4'), ('4+', '4+'))

    # models
    photo = models.ImageField(upload_to='model_photo')
    description = models.TextField()
    nickname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    appearance = models.CharField(choices=CHOICE_APPEARANCE, max_length=20)  # внешность
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    eyes = models.CharField(choices=CHOICE_EYES, max_length=20)
    hairs = models.CharField(choices=CHOICE_HAIRS, max_length=20)
    type = models.CharField(choices=CHOICE_TYPE, max_length=20)
    area = models.CharField(max_length=100, null=True, blank=True)
    breast = models.CharField(choices=CHOICE_BREAST, max_length=20)  # грудь
    phone_number = models.CharField(max_length=16)
    schedule = models.CharField(max_length=19)  # график работы
    speak_english = models.BooleanField(default=False)
    is_trans = models.BooleanField(default=False)
    in_osh = models.BooleanField(default=False)
    # gallery = models.ForeignKey(Gallery, )

    # services
    basic_service = models.ManyToManyField(BasicService)
    additional_service = models.ManyToManyField(AdditionalService, blank=True)  # доп услуги
    massage = models.ManyToManyField(Massage, blank=True)
    extreme = models.ManyToManyField(Extreme, blank=True)
    sadomazo = models.ManyToManyField(SadoMazo, blank=True)
    striptease = models.ManyToManyField(Striptease, blank=True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

#
#     @property
#     def rating(self):
#         all_stars = [review.stars for review in self.reviews.all()]
#         return round(sum(all_stars) / len(all_stars), 2) if len(all_stars) > 0 else 0
#
#
# class Review(models.Model):
#     CHOICE = ((i, '*' * i) for i in range(1, 6))
#     stars = models.IntegerField(choices=CHOICE)
#     text = models.CharField(max_length=255)
#     model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='reviews')
#
#     def __str__(self):
#         return self.model.name
#
#     @property
#     def model_name(self):
#         return self.model.name

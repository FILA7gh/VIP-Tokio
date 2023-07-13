from django.db import models


class BasicService(models.Model):
    CHOICES = (('Yes', 'Да'), ('No', 'Нет'))

    classic_sex = models.BooleanField(default=False, blank=True, verbose_name='Классический секс')
    condom_blowjob = models.BooleanField(default=False, blank=True, verbose_name='Минет с презервативом')
    cunnilingus = models.BooleanField(default=False, blank=True, verbose_name='Кунилингус')
    group_sex = models.BooleanField(default=False, blank=True, verbose_name='Групповой секс')
    lesbian_sex = models.BooleanField(default=False, blank=True, verbose_name='Лесбийский секс')
    blowjob_without_condom = models.CharField(choices=CHOICES, max_length=10, blank=True,
                                              verbose_name='Минет без презерватива')
    anal_sex = models.CharField(choices=CHOICES, max_length=10, blank=True, verbose_name='Анальный секс')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Основная услуга'
        verbose_name_plural = 'Основные услуги'


class AdditionalService(models.Model):
    cum_in_mouth = models.BooleanField(default=False, blank=True, verbose_name='Кончить в рот')
    cum_on_face = models.BooleanField(default=False, blank=True, verbose_name='Кончить на лицо')
    deep_blowjob = models.BooleanField(default=False, blank=True, verbose_name='Глубокий минет')
    toys = models.BooleanField(default=False, blank=True, verbose_name='Игрушки')
    role_playing_games = models.BooleanField(default=False, blank=True, verbose_name='Ролевые игры')
    services_for_couples = models.BooleanField(default=False, blank=True, verbose_name='Услуги семейной паре')
    photo_video_shooting = models.BooleanField(default=False, blank=True, verbose_name='Фото/видео съемка')
    escort = models.BooleanField(default=False, blank=True, verbose_name='Сопровождение')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Дополнительная услуга'
        verbose_name_plural = 'Дополнительные услуги'


class Massage(models.Model):
    relaxing_massage = models.BooleanField(default=False, blank=True, verbose_name='Расслабляющий массаж')
    classic_massage = models.BooleanField(default=False, blank=True, verbose_name='Классический массаж')
    pro_massage = models.BooleanField(default=False, blank=True, verbose_name='Профессиональный массаж')
    thai_massage = models.BooleanField(default=False, blank=True, verbose_name='Тайский массаж')
    prostate_massage = models.BooleanField(default=False, blank=True, verbose_name='Массаж простаты')
    erotic_massage = models.BooleanField(default=False, blank=True, verbose_name='Эротический массаж')
    sakura_branch = models.BooleanField(default=False, blank=True, verbose_name='Ветка сакуры')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Массаж'
        verbose_name_plural = 'Массажи'


class Striptease(models.Model):
    striptease_pro = models.BooleanField(default=False, blank=True, verbose_name='Стриптиз профи')
    striptease_not_pro = models.BooleanField(default=False, blank=True, verbose_name='Стриптиз не профи')
    candid_lesbian_show = models.BooleanField(default=False, blank=True, verbose_name='Откровенное лесби-шоу')
    easy_lesbian_show = models.BooleanField(default=False, blank=True, verbose_name='Легкое лесби шоу')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Стриптиз'
        verbose_name_plural = 'Стриптизы'


class SadoMazo(models.Model):
    bandage = models.BooleanField(default=False, blank=True, verbose_name='Бандаж')
    mistress = models.BooleanField(default=False, blank=True, verbose_name='Госпожа')
    slave = models.BooleanField(default=False, blank=True, verbose_name='Рабыня')
    light_domination = models.BooleanField(default=False, blank=True, verbose_name='Легкая доминация')
    flogging = models.BooleanField(default=False, blank=True, verbose_name='Порка')
    fetish = models.BooleanField(default=False, blank=True, verbose_name='Фетиш')
    trampling = models.BooleanField(default=False, blank=True, verbose_name='Трамплинг')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Садо Мазо'
        verbose_name_plural = 'Садо Мазо'


class Extreme(models.Model):
    anilingus = models.BooleanField(default=False, blank=True, verbose_name='Анилингус')
    golden_rain_issuance = models.BooleanField(default=False, blank=True, verbose_name='Золотой дождь выдача')
    golden_rain_reception = models.BooleanField(default=False, blank=True, verbose_name='Золотой дождь прием')
    strapon = models.BooleanField(default=False, blank=True, verbose_name='Страпон')
    fisting_anal = models.BooleanField(default=False, blank=True, verbose_name='Фистинг анальный')
    fisting_vaginal = models.BooleanField(default=False, blank=True, verbose_name='Фистинг вагинальный')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Экстрим'
        verbose_name_plural = 'Экстримы'


class PackagePrice(models.Model):
    apartments_1h = models.PositiveIntegerField(blank=True, default=0, verbose_name='Апартаменты 1 час')
    apartments_2h = models.PositiveIntegerField(blank=True, default=0, verbose_name='Апартаменты 2 часа')
    apartments_night = models.PositiveIntegerField(blank=True, default=0, verbose_name='Апартаменты ночь')
    departure_1h = models.PositiveIntegerField(blank=True, default=0, verbose_name='Выезд 1 час')
    departure_2h = models.PositiveIntegerField(blank=True, default=0, verbose_name='Выезд 2 часа')
    departure_night = models.PositiveIntegerField(blank=True, default=0, verbose_name='Выезд ночь')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Пакет цен'
        verbose_name_plural = ' Пакеты цен'

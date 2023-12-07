from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.settings import MIN_VALUE_RATING, MAX_VALUE_RATING


Users = get_user_model()


class Comics(models.Model):
    title = models.CharField(
        verbose_name='Название комикса',
        max_length=100
    )
    author = models.CharField(
        verbose_name='Автор',
        max_length=100
    )
    rating = models.FloatField(
        verbose_name='Рейтинг',
        validators=[MinValueValidator(MIN_VALUE_RATING), MaxValueValidator(MAX_VALUE_RATING)],
        default=0,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = '"Комикс"'
        verbose_name_plural = 'Комиксы'

    def __str__(self) -> str:
        return self.title


class Ratings(models.Model):
    """
    Модель рейтинга для отдельного комикса от пользователя
    """
    comics = models.ForeignKey(
        verbose_name='Комикс',
        to=Comics,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    user = models.ForeignKey(
        verbose_name='Пользователь',
        to=Users,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    value = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        verbose_name = 'объект "Оценка"'
        verbose_name_plural = 'оценки'

    def __str__(self) -> str:
        return f'[{self.user}: {self.value}] {self.comics}'


@receiver(post_save, sender=Ratings)
def update_rating(sender, instance: Ratings, *args, **kwargs):
    comics_title = instance.comics.title
    comics = Comics.objects.get(title=comics_title)
    avg_rating = comics.ratings.aggregate(value=Avg('value'))
    comics.rating = avg_rating['value']
    comics.save()

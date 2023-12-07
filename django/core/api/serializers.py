from rest_framework import serializers

from comics.models import Ratings, Comics
from core.settings import MIN_VALUE_RATING, MAX_VALUE_RATING


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('comics', 'user', 'value')


    def validate_value(self, attrs):
        if not (MIN_VALUE_RATING <= attrs <= MAX_VALUE_RATING):
            return serializers.ValidationError('Рейтинг не входит в требуемый диапазон')
        return attrs


class ReadonlyRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('value',)
        read_only_fields = ('value',)


class ComicsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comics
        fields = ('pk', 'title', 'author', 'rating')

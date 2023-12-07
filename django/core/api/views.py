from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from api.serializers import RatingsSerializer, ComicsSerializers, ReadonlyRatingSerializer
from comics.models import Ratings, Comics


class RatingsViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer

    def create(self, request, *args, **kwargs):
        serializer = RatingsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        comics_id = serializer.validated_data['comics']
        user_id = serializer.validated_data['user']

        try:
            obj = Ratings.objects.get(comics_id=comics_id, user_id=user_id)
        except Ratings.DoesNotExist:
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        obj.value = serializer.data['value']
        obj.save()
        return Response(status=status.HTTP_200_OK)


class ComicsViewSet(viewsets.ModelViewSet):
    queryset = Comics.objects.all()
    http_method_names = ['get']

    @action(methods=['GET'], detail=True, url_path='rating')
    def personal_rating(self, request, pk):
        obj = get_object_or_404(Comics, pk=pk).ratings.aggregate(value=Avg('value'))
        serializer = ReadonlyRatingSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if self.action == 'rating':
            return ReadonlyRatingSerializer
        return ComicsSerializers

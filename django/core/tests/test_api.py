import pytest
from rest_framework import status

from comics.models import Ratings


@pytest.mark.django_db
class Test00Ratings:
    URL_POST_RATING = '/api/v1/ratings/'

    def test_00_nodata_post(self, client):
        response = client.post(self.URL_POST_RATING)

        assert response.status_code != status.HTTP_404_NOT_FOUND, (
            f'Эндпоинт `{self.URL_POST_RATING}` не найден. Проверьте настройки '
            'в *urls.py*.'
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST, (
            f'Если POST-запрос, отправленный на эндпоинт `{self.URL_POST_RATING}`, '
            'не содержит необходимых данных, должен вернуться ответ со '
            'статусом 400.'
        )

        response_json = response.json()
        empty_fields = ['comics', 'user', 'value']
        for field in empty_fields:
            assert (field in response_json), (
                f'Если в POST-запросе к `{self.URL_POST_RATING}` не переданы '
                'необходимые данные, в ответе должна возвращаться информация '
                'об обязательных для заполнения полях.'
            )


    def test_01_invalid_post_data(self, client):
        invalid_form = {
            'comics': '1',
            'user': '1',
            'value': '1'
        }

        response = client.post(self.URL_POST_RATING, data=invalid_form)
        assert response.status_code == status.HTTP_400_BAD_REQUEST, (
            f'Если в POST-запросе к `{self.URL_POST_RATING}` передан '
            'невалидный данные, то сервер должен возвращать ответ со статусом 400'
        )

    def test_02_valid_post_data(self, reader, comics, reader_client, valid_form):
        response = reader_client.post(self.URL_POST_RATING, data=valid_form)

        assert response.status_code == status.HTTP_201_CREATED, (
            f'Если в POST-запросе к `{self.URL_POST_RATING}` переданы'
            f'валидные данные, то сервер должен возвращает ответ со статусом 201'
        )
        assert Ratings.objects.count() == 1, (
            f'Если в POST-запросе к `{self.URL_POST_RATING}` переданы'
            f'валидные данные, то сервер должен создавать объект'
        )

        assert Ratings.objects.last().value == valid_form['value'], (
            f'Если в POST-запросе к `{self.URL_POST_RATING}` переданы'
            f'валидные данные, то поле `value` должно обновиться'
        )

    def test_03_update_user_rating(self, reader_client, comics, valid_form):
        reader_client.post(self.URL_POST_RATING, data=valid_form)
        rating = Ratings.objects.last()
        old_value = rating.value

        valid_form['value'] = 1
        reader_client.post(self.URL_POST_RATING, data=valid_form)

        rating.refresh_from_db()
        new_value = rating.value

        assert old_value != new_value, (
            f'Если в POST-запросе к `{self.URL_POST_RATING}` у '
            f'объекта уже имеется запись, то поле `value` должно обновиться'
        )



@pytest.mark.django_db
class Test01Comics:
    URL_RATING_BY_COMICS = '/api/v1/comics/1/rating/'

    def test_00_get_current_rating(self, client, five_ratings_by_user):
        list_of_ratings = list(range(1, 6))
        current_avg_rating = sum(list_of_ratings) / len(list_of_ratings)
        response = client.get(self.URL_RATING_BY_COMICS)
        assert response.status_code == status.HTTP_200_OK, (
            f'При GET-запросе к `{self.URL_RATING_BY_COMICS}` '
            f'сервер должен возвращать ответ со статусом `200`'
        )

        response_json = response.json()
        assert 'value' in response_json and len(response_json) == 1, (
            f'При GET-запросе к `{self.URL_RATING_BY_COMICS}` '
            f'сервер должен возвращать ответ с полем `value`.'
        )
        assert response_json['value'] == current_avg_rating, (
            f'При GET-запросе к `{self.URL_RATING_BY_COMICS}` '
            f'сервер должен возвращать в поле `value` значение среднего рейтинга'
        )

import pytest

from comics.models import Ratings, Comics
from users.models import Users


@pytest.fixture
def comics():
    return Comics.objects.create(title='Title 1', author='Author 1', rating=0)


@pytest.fixture
def reader(django_user_model):
    return django_user_model.objects.create(username='Reader')

@pytest.fixture
def reader_client(reader, client):
    client.force_login(reader)
    return client

@pytest.fixture
def five_users(django_user_model):
    all_users = [django_user_model(username=f'Username {i}') for i in range(1, 6)]
    users = django_user_model.objects.bulk_create(all_users)
    return users


@pytest.fixture
def five_ratings_by_user(comics, five_users, django_user_model):
    all_ratings = [Ratings(comics=comics, user=five_users[i-1], value=i) for i in range(1, 6)]
    ratings = Ratings.objects.bulk_create(all_ratings)
    return ratings


@pytest.fixture
def valid_form(comics, reader):
    valid_form = {
        'comics': comics.id,
        'user': reader.id,
        'value': 5
    }
    return valid_form
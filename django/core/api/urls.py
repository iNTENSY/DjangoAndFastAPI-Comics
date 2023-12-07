from django.urls import path, include
from rest_framework import routers

from api import views


app_name = 'api'

router = routers.DefaultRouter()
router.register(r'comics', views.ComicsViewSet, basename='comics')
router.register(r'ratings', views.RatingsViewSet, basename='ratings')


urlpatterns = [
    path('v1/', include(router.urls))
]

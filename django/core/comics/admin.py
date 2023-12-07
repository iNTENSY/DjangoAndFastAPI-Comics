from django.contrib import admin

from comics.models import Comics, Ratings


@admin.register(Comics)
class ComicsAdmin(admin.ModelAdmin):
    pass


@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

# Register your models here.

from watchlist.models import Review, WatchList, StreamPlatform

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)



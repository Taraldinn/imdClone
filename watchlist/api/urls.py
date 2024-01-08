from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist.api.views import StreamPlatformViewSets, ReviewList, ReviewDetail, ReviewCreate, WatchlistViewSet

router = DefaultRouter()
router.register('stream', StreamPlatformViewSets, basename='streamplatform')
router.register('list', WatchlistViewSet, basename='watchlist')

urlpatterns = [

    # path("list/", WatchListAV.as_view(), name='movie-list'),
    # path("list/<int:pk>/", WatchDetailAV.as_view(), name='movie-detail'),
    # path("stream/", StreamPlatformAV.as_view(), name='stream-list'),
    # path("stream/<int:pk>/", StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    path('', include(router.urls)),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-detail'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-list'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),

]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist.api.views import StreamPlatformViewSets, ReviewList, ReviewDetail, ReviewCreate, UserReview, WatchlistViewSet

router = DefaultRouter()
router.register('stream', StreamPlatformViewSets, basename='streamplatform')
router.register('list', WatchlistViewSet, basename='watchlist')

urlpatterns = [

    path('', include(router.urls)),
    # path('list/', WatchlistViewSet.as_view({'get': 'list'}), name='movie-list'),
    # path("list/<int:pk>/", WatchlistViewSet.as_view({'get': 'list'}), name='movie-detail'),
    # path("stream/", StreamPlatformViewSets.as_view({'get': 'list'}), name='stream-list'),
    # path("stream/<int:pk>/", StreamPlatformViewSets.as_view({'get': 'list'}), name='streamplatform-detail'),
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-detail'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-list'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('reviews/',UserReview.as_view(),name='user-review' )

]

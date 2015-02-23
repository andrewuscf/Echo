from django.conf.urls import url, include, patterns
from rest_framework import routers
from Main.api import views

# Router sets up some urls automatically.
# So we can add them in batches
router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'track', views.TrackViewSet)
router.register(r'album', views.AlbumViewSet)
router.register(r'playlist', views.PlaylistViewSet)
router.register(r'user_music', views.UserMusicViewSet)
router.register(r'friend', views.FriendViewSet)
router.register(r'friendship_request', views.FriendshipRequestViewSet)

# Wire up API using automatic URL routing.
# Additionally, include login URLs for the browsable API

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^blap$', views.UserListAPIView.as_view()),

)
from django.urls import path
from .views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),
]

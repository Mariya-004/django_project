from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class RegisterView(CreateAPIView):
    queryset = User.objects.all()  # ✅ VERY IMPORTANT
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # ✅ OVERRIDES GLOBAL PERMISSION
    authentication_classes = []
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['author__username']  # optional filtering

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

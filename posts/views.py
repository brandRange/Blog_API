
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets #importing viewsets instead of generics
#also we change the four classes to just two since viewset makes available both list and detail

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer,UserSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PostDetail(viewset.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
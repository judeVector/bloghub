from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetailDelete(generics.RetrieveDestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

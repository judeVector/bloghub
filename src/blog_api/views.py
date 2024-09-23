from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, viewsets
from blog.models import Post

from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    AllowAny,
)

from .serializers import PostSerializer
from .permissions import PostUserWritePermission


# # Using generics
# class PostListCreate(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer

#     # def get_queryset(self):
#     #     user = self.request.user
#     #     return Post.objects.filter(author=user)

#     def perform_create(self, serializer):
#         if serializer.is_valid():
#             serializer.save(author=self.request.user)
#         return super().perform_create(serializer)


# class PostDetailDelete(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return Post.objects.filter(author=user)


# ViewSet
# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)

#     def create(self, request):
#         serializer_class = PostSerializer(data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return Response(serializer_class.data)
#         return Response("Error creating post")


# Model ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    lookup_field = "slug"

    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug)

    def get_queryset(self):
        return Post.objects.all()

from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "author",
            "excerpt",
            "image",
            "content",
            "status",
            "slug",
        )
        # extra_kwargs = {"author": {"read_only": True}}

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Category

User = get_user_model()


class PostModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="django")
        self.user = User.objects.create_user(
            username="testuser1", password="password123"
        )
        self.post = Post.objects.create(
            category=self.category,
            title="Post Title",
            excerpt="Post excerpt",
            author=self.user,
            content="Post content",
            slug="post-title",
            status="published",
        )

    def test_post_content(self):
        post = self.post

        # Check post content
        self.assertEqual(post.author.username, "testuser1")
        self.assertEqual(post.excerpt, "Post excerpt")
        self.assertEqual(post.title, "Post Title")
        self.assertEqual(post.content, "Post content")
        self.assertEqual(post.status, "published")
        self.assertEqual(str(post.category), "django")
        self.assertEqual(str(post), "Post Title")

    def test_slug_generation(self):
        # Test slug for a post with the same title (new instance)
        post2 = Post.objects.create(
            category=self.category,
            title="Post Title",
            excerpt="New Post excerpt",
            author=self.user,
            content="New Post content",
        )

        # First post should retain the slug as "post-title"
        self.assertEqual(self.post.slug, "post-title")

        # The second post with the same title should have a unique slug like "post-title-1"
        self.assertEqual(post2.slug, "post-title-1")

        # Additional post to confirm unique slug generation
        post3 = Post.objects.create(
            category=self.category,
            title="Post Title",
            excerpt="Another Post excerpt",
            author=self.user,
            content="Another Post content",
        )
        self.assertEqual(post3.slug, "post-title-2")

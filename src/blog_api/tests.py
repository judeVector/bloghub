from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Post, Category

User = get_user_model()


class PostTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="django")
        self.user = User.objects.create_user(
            username="testuser1", password="password123"
        )

        self.post = Post.objects.create(
            title="Exploring Django Models",
            author=self.user,
            excerpt="Initial excerpt",
            content="Initial content",
            status="published",
        )

        self.client.force_authenticate(user=self.user)
        print(self.post)

    def test_view_post(self):
        url = reverse("blog_api:listcreate")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        url = reverse("blog_api:listcreate")
        payload = {
            "title": "Exploring Django Models",
            "author": self.user.id,
            "excerpt": "This is a second test to see whether it will slug",
            "content": "This content is supposed to be sluggified in 2 number",
        }

        response = self.client.post(url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_post(self):
        url = reverse("blog_api:detailcreate", kwargs={"pk": self.post.id})
        payload = {
            "title": "Updated Django Models",
            "author": self.user.id,
            "excerpt": "This is an updated test to see whether it will slug",
            "content": "This content is going to be updated",
            "status": "published",
        }

        response = self.client.put(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

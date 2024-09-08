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

        user = User.objects.get(username="testuser1")
        self.client.force_authenticate(user=user)

    def test_view_post(self):
        url = reverse("blog_api:listcreate")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        url = reverse("blog_api:listcreate")
        payload = {
            "title": "Exploring Django Models",
            "author": 1,
            "excerpt": "This is a second test to see whether it will slug",
            "content": "This content is suppose to be sluggified in 2 number  ",
        }

        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

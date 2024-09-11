from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(status="published")

    options = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=60)
    excerpt = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=10, choices=options, default="published")

    objects = models.Manager()  # Default Manager
    postobjects = PostObjects()  # Custom Manager

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # If slug is not provided, generate one from the title
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            # Ensure the slug is unique by checking the database
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

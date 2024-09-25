from rest_framework.routers import DefaultRouter
from .views import PostViewSet, PostUpload
from django.urls import path

app_name = "blog_api"

# router = DefaultRouter()
# router.register("", PostViewSet, basename="post")
# urlpatterns = router.urls

urlpatterns = [path("create/", PostUpload.as_view(), name="post_upload")]

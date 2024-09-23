from rest_framework.routers import DefaultRouter
from .views import PostViewSet

app_name = "blog_api"

router = DefaultRouter()
router.register("", PostViewSet, basename="post")
urlpatterns = router.urls

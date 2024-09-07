from django.urls import path
from .views import *

urlpatterns = [
    path("", PostListCreate.as_view(), name="listcreate"),
    path("<int:pk>", PostDetailDelete.as_view(), name="detailcreate"),
]

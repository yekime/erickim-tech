from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .api import ProjectInfoViewSet
from .api import ExperienceViewSet

router = routers.DefaultRouter()
router.register(r"project-infos", ProjectInfoViewSet)
router.register(r"experiences", ExperienceViewSet)

urlpatterns = router.urls

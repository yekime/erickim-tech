from backend.models import ProjectInfo
from backend.models import Experience
from rest_framework import viewsets
from .serializers import ProjectInfoSerializer
from .serializers import ExperienceSerializer

# Project Info viewset
# allows us to create a CRUD api without specifying methods for functionality


class ProjectInfoViewSet(viewsets.ModelViewSet):

    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoSerializer


class ExperienceViewSet(viewsets.ModelViewSet):

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

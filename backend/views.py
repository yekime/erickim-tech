from urllib import request
from django.shortcuts import render
from backend.serializers import ProjectInfoSerializer
from backend.models import ProjectInfo
from rest_framework.response import Response
from rest_framework.views import APIView


# Unused
class ProjectInfosView(APIView):
    def get(self, request):
        project_infos = ProjectInfo.objects.all()
        serializer = ProjectInfoSerializer(project_infos, many=True)
        return Response(serializer.data)


# Unused
class ExperiencesView(APIView):
    def get(self, request):
        project_infos = ProjectInfo.objects.all()
        serializer = ProjectInfoSerializer(project_infos, many=True)
        return Response(serializer.data)

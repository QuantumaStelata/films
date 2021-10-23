from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from apps.database.models import Film
from .serializers import FilmsSerializer, FilmDetailSerializer


class FilmsViewSet(APIView):
    def get(self, request):
        queryset = Film.objects.filter(is_delete = False)
        serializer = FilmsSerializer(queryset, many = True, read_only = True)
        return Response(serializer.data)

class FilmDetailViewSet(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(Film, pk = pk, is_delete = False)
        serializer = FilmDetailSerializer(queryset, many = False, read_only = True)
        return Response(serializer.data)
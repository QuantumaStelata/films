from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404, get_list_or_404

from apps.database.models import Film
from .serializers import FilmsSerializer


class FilmsViewSet(APIView):
    def get(self, request):
        queryset = Film.objects.filter(is_delete = False)
        serializer = FilmsSerializer(queryset, many = True, read_only = True)
        return Response(serializer.data)
        

# class UrlDetailViewSet(APIView):
#     def get_obj(self, request, cut_url, is_delete = False):
#         if request.user.is_anonymous:
#             queryset = get_object_or_404(Url, cut_url = cut_url, creator_ip = request.META['REMOTE_ADDR'], is_delete = is_delete)
#         else:
#             queryset = get_object_or_404(Url, cut_url = cut_url, creator_user = request.user, is_delete = is_delete)

#         return queryset

#     def get(self, request, cut_url):
#         queryset = self.get_obj(request, cut_url)
#         serializer = UrlDetailSerializer(queryset)
#         return Response(serializer.data)

#     def delete(self, request, cut_url):
#         queryset = self.get_obj(request, cut_url)
#         queryset.is_delete = True
#         queryset.save()
#         return Response({'status': 'deleted'})  
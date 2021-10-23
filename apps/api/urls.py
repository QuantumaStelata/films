from django.urls import path
from .views import FilmsViewSet


urlpatterns = [
    path('films/', FilmsViewSet.as_view(), name='api-films'),
    # path('urls/<str:cut_url>/', UrlDetailViewSet.as_view()),
]
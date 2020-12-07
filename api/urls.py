from django.urls import path
from api.views import PersonasRecordView, MangasTodo, MangaDetail

app_name = 'api'
urlpatterns = [
    path('localuser/', PersonasRecordView.as_view(), name='localusers'),
    path('mangas/',  MangasTodo.as_view()),
    path('<int:pk>', MangaDetail.as_view())
]
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from mangas import views

urlpatterns = [


    path('revisar/', views.revisar, name="revisar"),
    path('new/', views.MangaCreate.as_view(), name='manga_form'),
    path('list/', views.MangaList.as_view(), name='manga_list'),
    path('view/<int:pk>', views.MangaDetail.as_view(), name='manga_detalle'),
    path('delete/<int:pk>', views.MangaDelete.as_view(), name='manga_delete'),
    path('edit/<int:pk>', views.MangaUpdate.as_view(), name='manga_update'),


]




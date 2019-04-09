from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^all_rooms/', views.RoomList.as_view(), name="all_rooms"),
    url(r'^room/new/$', views.add_room, name="room_new"),
    url(r'^room/delete/(?P<id>\d+)$', views.delete_room, name="room_delete"),
    url(r"^room/(?P<pk>\d+)", views.DetailRoom.as_view(), name="room_detail"),
    url(r'^room/modify/(?P<id>\d+)$', views.edit_room, name="room_modify"),
    url(r'^form/', views.form, name='form'),
    url(r'^search/', views.search, name='search'),
    url(r'^reservation/(?P<id>\d+)', views.reservation, name='reservation'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

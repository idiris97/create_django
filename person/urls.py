from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('persons/', person_view, name='person_view_url'),
    path('persons/<str:name>/', person_detail_view, name='person_detail_view_url'),
    path('create_person/', person_create, name='person_create_url'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
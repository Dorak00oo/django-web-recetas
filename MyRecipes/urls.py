from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name="index"),
    path('receta/<int:receta_id>/', views.receta, name="receta")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


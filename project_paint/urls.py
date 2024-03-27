from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from app_sectors import views

urlpatterns = [
    # path("admin/", admin.site.urls, name ="admin"),
    path("", views.initial, name="initial"),
    path("cadastro/", views.home, name="home"),
    path("clientes/", views.clientes, name="clientes"),
    path("insumos/", views.insumos, name="insumos"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

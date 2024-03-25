from django.urls import path

from app_sectors import views

urlpatterns = [
    # path("admin/", admin.site.urls, name ="admin"),
    path("", views.home, name="home"),
    path("clientes/", views.clientes, name="clientes"),
]

from django.urls import path
from . import views

urlpatterns = [
    # path(route, view,opt(kısayol ismi)),
    path('', views.index, name="index"),
]

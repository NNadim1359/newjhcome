from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="prothomalo"),
    path('kalerkantho/', views.kalerkantho_view, name="kalerkantho"),
]

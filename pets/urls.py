from django.urls import path, include
from pets import views


urlpatterns = [
    path("add", views.pet_add_view, name="add"),



]
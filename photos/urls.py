from django.urls import path,include
from photos import views


urlpatterns = [
    path('add', views.photo_add_view, name='photos-add'),
    path('<init:pk>/', include([
        path('', views.photo_details, name='photos-details'),
        path('edit/', views.photo_edit_view, name='photos-edit'),]))

]
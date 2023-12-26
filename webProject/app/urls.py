from django.urls import path
from . import views


urlpatterns = [
    
    path('<id>/', views.detail_view),
    path('create', views.create_view, name='create'),
    path('', views.list_view),
    path('<id>/update', views.update_view, name='update'),
    path('<id>/delete', views.delete_view, name='delete'),
]
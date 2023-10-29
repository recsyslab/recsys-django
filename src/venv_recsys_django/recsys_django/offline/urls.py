from django.urls import path
from . import views

app_name = 'offline'
urlpatterns = [
    path('update/', views.UpdateView.as_view(), name='update'),
]

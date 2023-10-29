from django.urls import path
from . import views

app_name = 'online'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('random/', views.RandomView.as_view(), name='random'),
    path('popularity/', views.PopularityView.as_view(), name='popularity'),
    path('<int:item_id>/similarity/', views.SimilarityView.as_view(), name='similarity'),
    path('itemcf/', views.ItemcfView.as_view(), name='itemcf'),
    path('<int:item_id>/rating/', views.RatingView.as_view(), name='rating'),
]
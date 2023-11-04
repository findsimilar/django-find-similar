"""
Urls for quickstart app
"""
from django.urls import path
from quickstart import views

app_name = 'quickstart'  # pylint: disable=invalid-name

urlpatterns = [
    path('', views.FindSimilarFormView.as_view(), name='find_similar'),
    path('results/', views.ResultListView.as_view(), name='results'),
]

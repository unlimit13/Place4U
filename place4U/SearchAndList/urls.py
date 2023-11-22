from django.urls import path

from . import views

app_name = "SearchAndList"
urlpatterns = [
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("results/<int:tag_id>/<str:location>/", views.results, name="results"),
    path("results/<int:tag_id>/<str:location>/filtered=<int:like_threshold>/", views.filtered_results, name="filtered_results"),
    
    # ex: /polls/5/vote/
    path("recent/<int:tag_id>/", views.recent_results, name="recent"),
    path("recent/<int:tag_id>/filtered=<int:like_threshold>/", views.filtered_recent_results, name="filtered_recent_results"),
    
]
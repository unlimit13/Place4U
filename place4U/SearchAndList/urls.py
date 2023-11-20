from django.urls import path

from . import views

app_name = "SearchAndList"
urlpatterns = [
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("results/<int:tag_id>/<str:location>/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("recent/<int:tag_id>/", views.recent_results, name="vote"),
]
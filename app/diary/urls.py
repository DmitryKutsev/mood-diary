from diary import views
from django.urls import path

app_name = "diary"

urlpatterns = [
    path("", views.DiaryListView.as_view(), name="diary_list"),
    path("<int:pk>/", views.DiaryDetailView.as_view(), name="diary-details"),
]

from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('login', views.HomePageView.as_view()),
    # path("<int:pk>/", views.DiaryDetailsView.as_view()),
]
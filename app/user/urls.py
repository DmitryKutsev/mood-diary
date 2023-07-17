from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('login', views.HomePageView.as_view()),
    # path("<int:pk>/", views.DiaryDetailsView.as_view()),
    path('register', views.ChooseUserView.as_view(), name="register"),
    path('register_therapist', views.TherapistCreateView.as_view(), name="register_therapist"),
    path('register_patient', views.PatientCreateView.as_view(), name="register_patient"),
    path('register_supervisor', views.SupervisorCreateView.as_view(), name="register_supervisor"),
]

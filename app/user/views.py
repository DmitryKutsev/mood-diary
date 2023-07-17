from django.views.generic import TemplateView, CreateView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from user.forms import SignUpForm, PatientForm, SupervisorForm

from core.models import Patient, Therapist, Supervisor

from user.forms import TherapistForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'user/register.html'


class ChooseUserView(TemplateView):
    template_name = 'user/register.html'


class HomePageView(TemplateView):
    template_name = 'home.html'


class PatientCreateView(View):
    model = Patient
    template_name = 'home.html'


class SupervisorCreateView(CreateView):
    model = Supervisor
    fields = ["name"]


class TherapistCreateView(View):

    def get(self, request, *args, **kwargs):
        user_form = SignUpForm()
        therapist_form = TherapistForm()
        return render(request, 'user/register_therapist.html', {'user_form': user_form,
                                                                'therapist_form': therapist_form})

    def post(self, request, *args, **kwargs):
        user_form = SignUpForm(request.POST)
        therapist_form = TherapistForm(request.POST, request.FILES)

        if all([user_form.is_valid(), therapist_form.is_valid()]):
            user = user_form.save(commit=False)
            user.save()
            therapist = therapist_form.save(commit=False)
            therapist.user_profile = user
            therapist.save()

        return render(request, 'user/post_register.html')


class PatientCreateView(View):

    def get(self, request, *args, **kwargs):
        user_form = SignUpForm()
        patient_form = PatientForm()
        return render(request, 'user/register_patient.html', {'user_form': user_form,
                                                              'patient_form': patient_form})

    def post(self, request, *args, **kwargs):
        user_form = SignUpForm(request.POST)
        patient_form = PatientForm(request.POST, request.FILES)

        if all([user_form.is_valid(), patient_form.is_valid()]):
            user = user_form.save(commit=False)
            user.save()
            patient = patient_form.save(commit=False)
            patient.user_profile = user
            patient.save()

        return render(request, 'user/post_register.html')


class SupervisorCreateView(View):

    def get(self, request, *args, **kwargs):
        user_form = SignUpForm()
        supervisor_form = SupervisorForm()
        return render(request, 'user/register_supervisor.html', {'user_form': user_form,
                                                              'supervisor_form': supervisor_form})

    def post(self, request, *args, **kwargs):
        user_form = SignUpForm(request.POST)
        supervisor_form = SupervisorForm(request.POST, request.FILES)

        if all([user_form.is_valid(), supervisor_form.is_valid()]):
            user = user_form.save(commit=False)
            user.save()
            supervisor = supervisor_form.save(commit=False)
            supervisor.user_profile = user
            supervisor.save()

        return render(request, 'user/post_register.html')

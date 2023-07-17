from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from core.models import Supervisor, Therapist, Patient


class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = [
            'name',
            'email',
            ]


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['bio']


class TherapistForm(ModelForm):
    class Meta:
        model = Therapist
        fields = ['bio']


class SupervisorForm(ModelForm):
    class Meta:
        model = Supervisor
        fields = ['cv', 'bio', 'diploma']


# class UserCreationMultiForm(MultiModelForm):
#     form_classes = {
#         'user': UserCreationForm,
#         'profile': UserProfileForm,
#     }
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, Button
from django.forms import ModelForm
from .models import *
from django import forms
from django.forms.widgets import DateTimeInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = [
            'assigned_to',
        ]
        widgets = {
            'start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    helper = FormHelper()
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('title', css_class='form-control mt-2 mb-3'),
        Field('description', rows="3", css_class='form-control mb-3', required=False),
        Field('status', css_class='form-control mb-3'),
        Field('start_date', css_class='form-control mb-3', required=False),
        Field('end_date', css_class='form-control mb-3', required=False),
        Field('priority', css_class='form-control mb-3'),
        Field('project', css_class='form-control mb-3', required=False),
        Submit('submit', 'Submit', css_class='button white mt-3')
    )


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'mb-2 form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'mb-2 form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'mb-2 form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'mb-2 form-control', 'placeholder': 'Email'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'mb-2 form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'mb-2 form-control', 'placeholder': 'Confirm Password'})

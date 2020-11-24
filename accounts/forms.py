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
            'start_date': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_date': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
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


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'note'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'mb-2 form-control', 'placeholder': 'Title'}),
            'note': forms.Textarea(attrs={'class': 'mb-2 form-control', 'placeholder': 'Note'}),
        }


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


class ProjectTaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = [
            'assigned_to',
            'project'
        ]
        widgets = {
            'start_date': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_date': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = [
            'assigned_to',
        ]
        widgets = {
            'start_date': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_date': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'client_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'repo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        exclude = [
            'assigned_to',
        ]
        widgets = {
            'start_date': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_date': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'client_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'repo': forms.TextInput(attrs={'class': 'form-control'}),
        }

    helper = FormHelper()
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('title', css_class='form-control mt-2 mb-3'),
        Field('description', rows="3", css_class='form-control mb-3', required=False),
        Field('status', css_class='form-control mb-3'),
        Field('start_date', css_class='form-control mb-3', required=False),
        Field('end_date', css_class='form-control mb-3', required=False),
        Field('client_name', css_class='form-control mb-3'),
        Field('client_email', css_class='form-control mb-3', required=False),
        Field('repo', css_class='form-control mb-3'),
        Submit('submit', 'Submit', css_class='button white mt-3')
    )

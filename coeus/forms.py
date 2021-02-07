from django import forms

class InstallForm(forms.Form):
    website_name = forms.CharField(label='Website Name', max_length=50)
    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField(label='E-mail', max_length=255)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
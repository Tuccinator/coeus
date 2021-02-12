from django import forms

class NewProjectForm(forms.Form):
    name = forms.CharField(label='Project Name', max_length=100)
    slug = forms.CharField(label='Project Slug (optional)', max_length=100, required=False)
    description = forms.CharField(label='Project Description', widget=forms.Textarea())
from django import forms
from .models import Department, Course, Material, Gender, Purpose


class SubmissionForm(forms.Form):
    name = forms.CharField(max_length=50)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField()
    gender = forms.ModelChoiceField(queryset=Gender.objects.all())
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    purpose = forms.ModelChoiceField(queryset=Purpose.objects.all())
    materials_provide = forms.ModelMultipleChoiceField(queryset=Material.objects.all(),
                                                       widget=forms.CheckboxSelectMultiple)

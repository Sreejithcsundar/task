from django.shortcuts import render, redirect
from .models import Department, Course, Material, Student
from .forms import SubmissionForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def create_student(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form_submission = Student(
                name=form.cleaned_data['name'],
                dob=form.cleaned_data['dob'],
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
                department=form.cleaned_data['department'],
                course=form.cleaned_data['course'],
                purpose=form.cleaned_data['purpose'],

            )
            form_submission.save()
            form_submission.materials_provide.set(form.cleaned_data['materials_provide'])

            return redirect('success')
    else:
        form = SubmissionForm()
    return render(request, 'create_student.html', {'form': form})


def success(request):
    return render(request, 'success.html')



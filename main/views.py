from django.shortcuts import render
from .forms import StudentApplicationForm, TeacherApplicationForm

# Homepage view
def home(request):
    return render(request, 'main/home.html')

# Student Admission page
def admissions_student(request):
    return render(request, 'main/admissions_student.html')

def teacher_landing(request):
    return render(request, 'main/teacher_landing.html')


# Student application view
def apply_student(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST)
        if form.is_valid():
            applicant = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
        return render(request, 'main/application_success.html', {
    'applicant': applicant,
    'contact_number': form.cleaned_data['contact_number']
})


    else:
        form = StudentApplicationForm()
    
    return render(request, 'main/apply_student.html', {'form': form})

# Teacher application view
def apply_teacher(request):
    if request.method == 'POST':
        form = TeacherApplicationForm(request.POST)
        if form.is_valid():
           applicant = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
        return render(request, 'main/application_success.html', {
    'applicant': applicant,
    'contact_number': form.cleaned_data['contact_number']
})

    else:
        form = TeacherApplicationForm()
    
    return render(request, 'main/apply_teacher.html', {'form': form})

# Campus tour view
def campus_tour(request):
    return render(request, 'main/campus_tour.html')

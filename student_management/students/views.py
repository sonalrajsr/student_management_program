from django.shortcuts import render, redirect
from students.models import students
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):
    return render(request, "index.html")


def students_all(request):
    if request.method == 'GET':
        students_list = students.objects.all()
        contex = {
            'students_all' : students_list
        }
    return render(request, 'all_students.html', contex)

def add_students(request):
    if request.method == 'POST':
        # Get data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        roll_number = request.POST.get('roll_number')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')

        if students.objects.filter(roll_number=roll_number).exists() or students.objects.filter(email=email).exists():
            return render(request, 'add_student.html', {'error_message': 'A student with this roll number/Email already exists.'})

        # Create a new Student instance and save to the database
        new_student = students(
            first_name=first_name,
            last_name=last_name,
            department=department,
            roll_number=roll_number,
            email=email,
            date_of_birth=date_of_birth
        )
        new_student.save()

        return redirect('all_students')  # Redirect to all student page by name
    
    return render(request, 'add_student.html')

def update_students(request):
    try:
        if request.method == "POST":
            roll_number = request.POST.get('roll_number')            
            return redirect('update_by_roll_number', roll_number = roll_number)
    except ObjectDoesNotExist:
        error_message = "Student not found."
        return render(request, 'delete_student.html', {'error_message': error_message})
    return render(request, 'update_student.html')

def update_by_roll_number(request, roll_number):
    student_to_update = students.objects.get(roll_number = roll_number)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        roll_number = request.POST.get('roll_number')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')

        student_to_update.first_name = first_name
        student_to_update.last_name = last_name
        student_to_update.department = department
        student_to_update.roll_number = roll_number
        student_to_update.email = email
        student_to_update.date_of_birth = date_of_birth
        student_to_update.save()
        return redirect('all_students')
    return render(request, 'update_by_roll.html', {'student' : student_to_update})


@permission_required('students.delete_student', raise_exception=True)
def remove_students(request):
    students_to_delete = None
    try:
        if request.method == "POST":
            roll_number = request.POST.get('roll_number')
            students_to_delete = students.objects.get(roll_number=roll_number)
            students_to_delete.delete()
            return redirect('all_students')
    except ObjectDoesNotExist:
        error_message = "Student not found."
        return render(request, 'delete_student.html', {'error_message': error_message})
    return render(request, 'delete_student.html',{'student' : students_to_delete})

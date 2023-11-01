from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from .models import Courses,Event,Teacher,Curriculum,Student,Contact
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        courses = Courses.objects.all()
        events = Event.objects.all()
        context["events"] = events
        context["courses"] = courses
        return context

def CourseDetails(request, id):
    user = request.user
    request.session['courseID'] = id
    course = get_object_or_404(Courses, id=id)
    teacher = Teacher.objects.get(courses=course)
    syllabus = Curriculum.objects.filter(course=course)
    student = get_object_or_404(Student,user=user)
    most_recent_highest_id_object = Curriculum.objects.order_by('-id').first()
    context = {'course': course,'teacher': teacher,'syllabus':syllabus,'student':student,'date':most_recent_highest_id_object}
    return render(request, 'course.html', context)


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user using Django's built-in authentication
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Use the renamed auth_login function to log the user in
            auth_login(request, user)
            return HttpResponse('login successfully')
        else:
            return HttpResponse('login failed')
    else:
        return render(request, 'sign-in.html')

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login

class SignUp(View):
    def get(self, request, *args, **kwargs):
        # Display the sign-up form for GET requests
        return render(request, 'sign-up.html')

    def post(self, request, *args, **kwargs):
        # Get user input from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new user
        User.objects.create_user(username=f"{first_name} {last_name}", first_name=first_name, last_name=last_name, email=email, password=password)
        user = User.objects.get(username=f"{first_name} {last_name}")
        # Log the user in
        login(request, user)

        return redirect('/student-creation/')  # Redirect to the user's profile page or another suitable page



def student_creation(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Process the form data and create a Student object (your existing code)
            name = request.user.first_name
            user = request.user
            student_image = request.POST.get('student_image')
            age = request.POST.get('age')
            teacher_language = request.POST.get('Teacher_language')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            Student.objects.create(user=user, student_image=student_image, name=name, age=age, Teacher_language=teacher_language, start_time=start_time, end_time=end_time)
            return redirect('/profile/')
        elif request.method == 'GET':
            # This is a GET request, so render the HTML form
            return render(request, 'student_creation.html')
    else:
        return redirect('/login/')


from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist  # Import the exception
class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        student = Student.objects.get(user=user)

        try:
            teacher = Teacher.objects.get(courses=student.course)
        except Teacher.DoesNotExist:
            teacher = []  # Set teacher to an empty list if not found

        context['student'] = student
        context['teacher'] = teacher
        return context

class Courses_view(TemplateView):
    template_name = 'courselist.html'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["data"] = Courses.objects.all()
        return context


class About(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teachers = Teacher.objects.all()
        courses = Courses.objects.all()
        context["Teachers"] = teachers
        context["Courses"] = courses
        return context



class ContactView(TemplateView):
    template_name = 'contact.html'

    def post(self, request):
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')

        # Create and save a new Contact object
        contact = Contact(name=name, subject=subject, email=email, number=number, message=message)
        contact.save()

        return redirect(f'https://wa.me/+971562579164?text=Email Query : {name}, {email}, message : {message}')

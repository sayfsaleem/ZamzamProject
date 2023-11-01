from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
urlpatterns = [
    path('', views.HomeView.as_view(),name='Home'),
    path('course/<int:id>/', views.CourseDetails, name='Course Details'),
    path('login/',views.custom_login,name='Login'),
    path('signup/',views.SignUp.as_view(),name='Sign Up'),
    path('student-creation/',views.student_creation,name='student Creation'),
    path('profile/',views.Profile.as_view(),name='Profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('courses/',views.Courses_view.as_view(), name='Course'),
    path('about/',views.About.as_view(), name='About'),
    path('contact/',views.ContactView.as_view(), name='Contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

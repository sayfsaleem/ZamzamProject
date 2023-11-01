from django.db import models
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User
# Create your models here.
class Courses(models.Model):
    Choices = (
        ('Quran Memorization','Quran Memorization'),
        ('Quran Recictation with Tajweed','Quran Recictation with Tajweed'),
        ('Alim Course','Alim Course'),
        ('Hadith Course','Hadith Course'),
        ('Tafseer ul Quran','Tafseer ul Quran'),
    )
    Languages = (
        ('English','English'),
        ('Urdu','Urdu'),
        ('Arabic','Arabic'),
    )
    course_name = models.CharField(max_length=40,verbose_name='Course Name', blank=False,null=False,help_text="Course Name",choices=Choices)
    course_image = models.ImageField(null=False, blank=False,upload_to='course_images/')
    language = models.CharField(max_length=40,verbose_name='Language', blank=False,null=False,help_text="Language",choices=Languages)
    brief =  FroalaField()
    weeks = models.PositiveIntegerField(null=False, blank=False,default=1)
    price = models.FloatField(null=False, blank=False,verbose_name="Price of Course",help_text="Price of Course")
    lessons = models.PositiveIntegerField(null=False, blank=False,default=1)
    def __str__(self):
        return self.course_name
class Teacher(models.Model):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    teacher_image = models.ImageField(upload_to='image/teacher/')
    Choices = (
        ('Male','Male'),
        ('Female','Female'),
    )
    name = models.CharField(max_length=90,verbose_name='Teacher Name', blank=False,null=False,help_text="Teacher's Name")
    gender = models.CharField(max_length=10,verbose_name='Teacher Gender',blank=False,null=False,help_text="Teacher's Gender",choices=Choices)
    nationality = models.CharField(max_length=20,verbose_name='Teacher Nationality',blank=False,null=False,help_text="Teacher's Nationality")
    courses = models.ManyToManyField(Courses)
    Bio = models.TextField(max_length=700,verbose_name='Bio', blank=False,null=False,help_text='Bio of Teacher')
    def __str__(self):
        return self.name



class Student(models.Model):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    student_image = models.ImageField(upload_to='students')
    name =  models.CharField(max_length=50,verbose_name='Student Name', blank=False,null=False,help_text='Student Name')
    course = models.ForeignKey(Courses,verbose_name='Student Chosen Course', blank=False,null=True,help_text='Student Selected Course',on_delete=models.SET_NULL)
    age = models.IntegerField(help_text="Student's age",verbose_name='Student age',null=False,blank=False)
    Teacher_language = models.CharField(max_length=90,blank=False,null=False,verbose_name="Student's Chosen Language",help_text="student's chosen language")
    start_time = models.TimeField(verbose_name="Start Time", blank=False, null=False,help_text="Student avaiable at that Time")
    end_time = models.TimeField(verbose_name="End Time", blank=False, null=False,help_text="Student available time ended at")
    current_remarks = models.TextField(verbose_name="How's Student Studying",blank=True,null=True,help_text="Student's Progress in Following Course - You hae to update it weekly.")
    paid = models.BooleanField(verbose_name="Student Paid The Fees ?",default=False)


class Event(models.Model):
    picture = models.ImageField(upload_to='eventimage/',null=False,blank=False)
    location = models.CharField(max_length=40,null=False, blank=False)
    title = models.CharField(max_length=70,null=False, blank=False)
    time = models.TimeField()
    link = models.URLField(blank=True,null=False)

class Curriculum(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)  # Link the curriculum to a specific course
    week_number = models.PositiveIntegerField()  # Week number
    title = models.CharField(max_length=100)  # Week title
    date = models.DateField()  # Date of the week's session
    time = models.TimeField()  # Time of the week's session
    zoom_link = models.URLField()  # Zoom link for the week's session

    def __str__(self):
        return f"Week {self.week_number} - {self.title}"



class Contact(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    subject = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(max_length=90,null=False,blank=False)
    number = models.CharField(max_length=15,null=False,blank=False)
    message = models.TextField(null=False,blank=False)

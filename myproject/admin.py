from django.contrib import admin
from onlinecourse.models import Question, Choice, Submission ,Enrollment,Lesson,Course,Learner,Instructor

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Learner)
admin.site.register(Instructor)

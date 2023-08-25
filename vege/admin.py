from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Reciepe)



admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)

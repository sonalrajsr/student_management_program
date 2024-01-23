from django.contrib import admin
from students.models import students
# Register your models here.

class studentsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'roll_number','department', 'date_of_birth')  # Customize the displayed fields
    # search_fields = ('field1', 'field2')
admin.site.register(students, studentsAdmin)
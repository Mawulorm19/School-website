from django.contrib import admin
from .models import SchoolInfo, Announcement, Course, ContactInfo


admin.site.register(SchoolInfo)
admin.site.register(Announcement)
admin.site.register(Course)
admin.site.register(ContactInfo)

# Register your models here.

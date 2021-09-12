from django.contrib import admin
from home.models import Contact
from home.models import Project,Services,About

# Register your models here.
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Services)
admin.site.register(About)
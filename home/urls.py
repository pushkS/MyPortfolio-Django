from django.contrib import admin
from django.urls import path, include
from home import views


#admin log-in customization

admin.site.site_header = "pushkR Portfolio"
admin.site.site_title = "Welcome to pushk Dashboard"
admin.site.index_title = "Welcome to my Portal"
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('resume', views.resume, name='resume'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]
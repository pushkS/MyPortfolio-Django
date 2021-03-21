from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.URLField( max_length=400,null=True,blank=True)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
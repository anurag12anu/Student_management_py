from django.db import models

class Student_Model(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=100)
    branch=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    
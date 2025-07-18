from django.contrib import admin
from .Model.auth_model import Auth_Session_Model
from .Model.student_model import Student_Model

admin.site.register(Auth_Session_Model)
admin.site.register(Student_Model)

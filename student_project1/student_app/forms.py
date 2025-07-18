from .Model.student_model import Student_Model
from django import forms

class Student_forms(forms.ModelForm):
    class Meta:
        model=Student_Model
        fields='__all__'
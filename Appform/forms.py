from django import forms
from Appform.models import Students
class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__' 
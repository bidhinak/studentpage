from django import forms
from django.contrib.auth.forms import UserCreationForm

from stdapp.models import Login, student, teacher, marksadd


class Customform(UserCreationForm):
    username=forms.CharField()
    password1 =forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)
    class Meta:
        model=Login
        fields=("username","password1","password2")

class DateInput(forms.DateInput):
    input_type = 'date'

class studentform(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput)

    class Meta:
        model=student
        fields="__all__"
        exclude=("one",)

class teacherform(forms.ModelForm):
    class Meta:
        model=teacher
        fields="__all__"
        exclude=("two",)

class marksaddform(forms.ModelForm):
    class Meta:
        model=marksadd
        fields="__all__"
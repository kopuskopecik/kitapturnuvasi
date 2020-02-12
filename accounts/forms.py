from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
#from django.contrib.auth.models import User

from .models import User, Teacher
#from .models import User

#class StudentSignUpForm(UserCreationForm):
    #etkinlik = forms.ModelChoiceField(
        #queryset= Etkinlik.objects.all(),
        #required=True
    #)
    #class Meta(UserCreationForm.Meta):
        #model = User
		

    #@transaction.atomic
    #def save(self):
       # user = super().save(commit=False)
        #print("")
        #user.is_student = True
        #user.save()
        #student = Student.objects.create(student=user, ogretmen = self.cleaned_data.get('etkinlik').ogretmen)
        #return user


class TeacherSignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    password1 = forms.CharField(label = "Parola", widget=forms.PasswordInput(attrs={'placeholder':'Parolanız en az 8 karakterden oluşmalıdır'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(teacher=user)
        return user
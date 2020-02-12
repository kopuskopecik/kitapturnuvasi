from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .forms import TeacherSignUpForm
from .models import User
#from django.contrib.auth.models import User

class SignUpView(TemplateView):
    template_name = 'accounts/signup.html'

class UyelikView(TemplateView):
	template_name = 'accounts/uyelik.html'
	
	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		if request.user.is_authenticated:
			return redirect('orders:order_create')
		else:
			return self.render_to_response(context)
		

#class StudentSignUpView(CreateView):
#    model = User
#    form_class = StudentSignUpForm
#    template_name = 'accounts/signup_form.html'

#    def get_context_data(self, **kwargs):
#        kwargs['user_type'] = 'student'
 #       return super().get_context_data(**kwargs)

  #  def form_valid(self, form):
   #     user = form.save()
    #    login(self.request, user)
     #   return redirect('anasayfa:anasayfa')

class TeacherSignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'accounts/signup_form.html'
    

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        next = self.request.GET.get('next', '/')
        messages.success(self.request, 'Hoşgeldiniz {}. Hesabınız başarıyla oluşturulmuştur'.format(self.request.user))
        return redirect(next)

@method_decorator(login_required, name='dispatch')
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')
    success_message = "Şifreniz başarıyla değiştirilmiştir."
	
    def get_object(self):
        return self.request.user



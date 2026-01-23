from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    # form_class attribute allows us to let django know the inputs of the form from any
    # other form ckass ti gabdke tge creation of objects
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

class ChangeMyPassword(CreateView):
    template_name = "registration/changemypassword.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm
from .models import SignUp

# Create your views here.
# def home(request):
# 	title = 'Welcome'
# 	form = SignUpForm(request.POST or None)
# 	context = {
# 		"form": form
# 	}
	
# 	# add a form
# 	if form.is_valid():
# 		form.save()
# 		context = {
# 			"title": "Thank you"
# 		}
	
# 	return render(request, "base.html", context)
def home(request):
	if request.method == 'POST' and form.is_valid:
		nameF = request.POST['name']
		emailF = request.POST['email']
		print(nameF)
		print(emailF)
		formInstance = SignUp(full_name = nameF, email = emailF)
		formInstance.save()
	return render(request, 'base.html')

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get('email')
		form_message = form.cleaned_data.get('message')
		form_full_name= form.cleaned_data.get('full_name')
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = 'j-kozlowski@live.com'
		contact_message = """{}: {} via {}""".format(
			form_full_name, 
			form_message, 
			form_email)
		
		send_mail(subject, 
				contact_message, 
				from_email, 
				[to_email], 
				fail_silently=False)
	context = {
		"form": form,
	}
	return render(request, "forms.html", context)
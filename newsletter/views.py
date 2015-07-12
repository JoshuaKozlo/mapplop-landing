from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import ContactForm
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
def get_client_ip(request):
    x_forwared_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwared_for:
        ip = x_forwared_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    if request.method == 'POST':
        nameF = request.POST['name']
        emailF = request.POST['email']
        user_typeF = request.POST['inlineRadioOptions']
        ipF = get_client_ip(request)
        if SignUp.objects.filter(email = emailF).exists():
            x = 'DO NOTHING'
        else:
            form_instance = SignUp(full_name = nameF, email = emailF, ip = ipF, user_type = user_typeF)
            form_instance.save()
            email_verification(nameF, emailF)
    return render(request, 'base.html')



def email_verification(name, email):
    subject = 'Thanks for joining the mapplop newsletter!'
    from_email = settings.EMAIL_HOST_USER
    to_email = email
    contact_message = "mapplop"
    send_mail(subject,
              contact_message,
              from_email,
              [to_email],
              fail_silently=False,
              html_message=render_to_string('email.html', {'name': name}))






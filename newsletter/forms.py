from django import forms

from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control"}))
	message = forms.CharField()



class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name

	

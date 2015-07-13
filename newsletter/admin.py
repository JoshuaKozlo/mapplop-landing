from django.contrib import admin

# Register your models here.

from .models import SignUp


class SignUpAdmin(admin.ModelAdmin):
	list_display = ('email', 'full_name', 'ip', 'user_type', 'timestamp')
	class Meta:
		model = SignUp
	




admin.site.register(SignUp, SignUpAdmin)

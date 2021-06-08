from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
   add_form = CustomUserCreationForm
   form = CustomUserChangeForm
   model = CustomUser
   list_display = ['username', 'email','password','is_staff', ] 


admin.site.register(CustomUser, CustomUserAdmin)
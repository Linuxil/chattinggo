from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .forms import UsersCreationForm,UsersChangeForm
from .models import *
# Register your models here.



# class UsersAdmin(admin.ModelAdmin):
#     add_form_ = UsersCreationForm
#     form = UsersChangeForm
#     model  = Users

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("first_name","username","last_active")

admin.site.register(Messages)
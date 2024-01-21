from django.shortcuts import render,redirect
from .models import Users, Messages

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView,UpdateView


class ChatView(View,):

    def get(self,request):
        users = Users.objects.all()
        context = {'users': users}
        print(request.user)
        return render(request,'index.html',context)
    # def post(request):
    #     pass
    # direct = Users.objects.get(id=id)
    # if request.method == "POST":
    #     message = request.POST.get('message')
    #     user = Users.objects.get(username=request.user.username)
    #     Messages.objects.create(sender=user, receiver=direct)

# def home2(request):
#     users = Users.objects.all()
#     # user = Users.objects.get(id=2)

#     context = {'users': users}

#     return render(request,'direct.html',context)



# class LoginView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request,'login.html')
class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    
    def post(self, request):
        print("posting login")
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not Users.objects.filter(username=username).exists():
            return redirect('/login')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        return redirect('/login')
    

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect( '/login')

    
    
    
class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'registration.html')  
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        Users.objects.create(username=username, first_name=first_name, password=password)
        return render(request,'registration.html')



class EditProfilView(UpdateView):
    template_name = "editProfil.html"
    model = Users
    fields = ("image","username","first_name","last_name","password")
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["form_title"] = "Mijoz ma'lumotlarini tahrirlash"
        context["button_title"] = "Saqlash"
        return context


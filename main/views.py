from django.shortcuts import render,redirect
from .models import Users, Messages

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView,UpdateView

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ChatView(View):
    @method_decorator(login_required)
    def get(self,request):
        user = Users.objects.get(username=request.user.username)
        print()
        print(user)
        print()
        users = Users.objects.exclude(id=user.id)

        context = {'users': users}

        return render(request,'index.html',context)
        

    def post(self,request):
        searchuser = request.POST.get('search')
        users = Users.objects.filter(username=searchuser)
        context = {'users': users}
        return render(request,'index.html',context)




class ChatdirectView(View):
    def get(self,request,user_pk):
        users = Users.objects.all()
        sender_user = Users.objects.get(username=request.user.username)
        receiver_user = Users.objects.get(id=user_pk)
        sender_messages = Messages.objects.filter(sender=sender_user,receiver=receiver_user)
        receiver_messages = Messages.objects.filter(receiver=sender_user,sender=receiver_user)

        all_messages = sender_messages | receiver_messages
        all_messages = all_messages.order_by('message_date')
        users = Users.objects.exclude(id=sender_user.id)
        context = {'users': users,'user': receiver_user}
        context['all_messages'] = all_messages
        return render(request,'direct.html',context)
    
    def post(self,request,user_pk):
        if 'forsearch' in request.POST:
            searchuser = request.POST.get('search')
            users = Users.objects.filter(username=searchuser)
            context = {'users': users}
            return render(request,'direct.html',context)
        else:
            sender_user = Users.objects.get(username=request.user.username)
            receiver_user = Users.objects.get(id=user_pk)
            message_body = request.POST.get('message')
            Messages.objects.create(sender=sender_user, receiver=receiver_user,message_body=message_body)
        
        return redirect('chat',user_pk=user_pk)


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
        user = Users.objects.create(username=username, first_name=first_name)
        user.set_password(password)
        user.save()
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


from django.shortcuts import render,redirect,get_object_or_404

from .Model.auth_model import Auth_Session_Model

from django.contrib.auth.hashers import check_password
from django.contrib.auth import login,logout as auth_logout
from django.http import HttpResponse



def login_user(request):
    
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        
        try:
            user=Auth_Session_Model.objects.get(username=username)
            if check_password(password , user.password):
                
                request.session['user_id']=user.id
                request.session['user_name']=user.username
                return redirect('dash')
            else:
                HttpResponse('invalid username or password')
                
        except Auth_Session_Model.DoesNotExist:
            HttpResponse('user data not found ')
        
        
        
    return render(request,'student_app/login.html')

def logout_user(request):
    request.session.flush()
    return redirect('logi')




def dashboard(request):
    if 'user_id' not in  request.session:
        return redirect('logi')
    return render(request,'student_app/dashboard.html')

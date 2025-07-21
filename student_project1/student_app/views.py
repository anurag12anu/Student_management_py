from django.shortcuts import render,redirect,get_object_or_404

from .Model.auth_model import Auth_Session_Model
from .Model.student_model import Student_Model
from .forms import Student_forms

from django.contrib.auth.hashers import check_password
from django.contrib.auth import login,logout as auth_logout
from django.http import HttpResponse
from django.db.models import Count,Q



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



def student_add(request):
    if request.method == 'POST':
        form =Student_forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        form =Student_forms()
    return render(request, 'student_app/add.html', {'form': form})
        
    
def student_update(request,pk):
    student =get_object_or_404(Student_Model,pk=pk)
    if request.method == 'POST':
        update_form =Student_forms(request.POST, instance=student)
        if update_form.is_valid():
            update_form.save()
            return redirect('dash')
    else:
        form =Student_forms(instance=student)
    return render(request,'student_app/update.html',{'form': form, 'students': student })



def student_delete(request,pk):
    student =get_object_or_404(Student_Model,pk=pk)
    
    if request.method == 'POST':
        student.delete()
        return redirect('dash')
    return render(request,'student_app/delete.html', { 'students':student})



def student_view(request,pk ):
    student =get_object_or_404(Student_Model,pk=pk)
    return render(request,'student_app/view.html',{'students':student})



def dashboard(request):
    if 'user_id' not in  request.session:
        
        return redirect('logi')
    
    query=request.GET.get("q","")
    
    students= Student_Model.objects.filter(
        Q(name__icontains=query)| Q(branch__icontains=query)
    ) if query else Student_Model.objects.all()
    
    total_students = students.count()
    branch_counts = students.values('branch').annotate(count=Count('branch'))
    branch_dict = {b['branch']: b['count'] for b in branch_counts}


    return render(request,'student_app/dashboard.html',{
        'student':students,
        'total_student':total_students,
        'branch_count':branch_dict,
        'request':request
        } )

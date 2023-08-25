from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.





#create query
@login_required(login_url="/login/")
def reciepies(request):
    if request.method=="POST":
        data=request.POST
        rec_image=request.FILES.get('reciepe_image')
        rec_name=data.get('reciepe_name')
        rec_desc=data.get('reciepe_description')
        
        
        Reciepe.objects.create(reciepe_name=rec_name,reciepe_description=rec_desc,reciepe_image=rec_image)
        
        return redirect('/vege/')
    
    
    #Read query
    queryset=Reciepe.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(reciepe_name__icontains=request.GET.get('search'))
    context={'reciepe':queryset}
    
        
       
    return render(request,'reciepe.html',context)


#delete query
@login_required(login_url="/login/")
def delete_reciepe(request,rec_id):

    queryset=Reciepe.objects.get(id=rec_id)
    import os
 
    # File name
    file = str(queryset.reciepe_image)
   
 
    # File location
    location = "public\static"
 
    # Path
    path = os.path.join(location, file)
 
    # Remove the file
    # 'file.txt'    
    os.remove(path)


    queryset.delete()
    print(queryset.reciepe_name,queryset.reciepe_description)
    return redirect('/vege/')
   # return HttpResponse(rec_id)


#update query
@login_required(login_url="/login/")
def update_reciepe(request,rec_id):
    queryset=Reciepe.objects.get(id=rec_id)
    if request.method=='POST':
        data=request.POST
        updated_rec_image=request.FILES.get('reciepe_image')
        updated_rec_name=data.get('reciepe_name')
        updated_rec_desc=data.get('reciepe_description')

        queryset.reciepe_name=updated_rec_name
        queryset.reciepe_description=updated_rec_desc
        if updated_rec_image:
            queryset.reciepe_image=updated_rec_image

        queryset.save()
        return redirect('/vege/')
    context={'recipe':queryset}
    return render(request,'updaterecipe.html',context)



 





def register_handel(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_name=request.POST.get('user_name')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=user_name)
        if user.exists():
            messages.info(request, "User name already taken")
            return redirect('/register/')
            
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=user_name
            )
        
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")
        return redirect('/register/')
        
    return render(request,'register.html')


def login_handel(request):
    if request.method=='POST':
        user_name=request.POST.get('user_name')
        password=request.POST.get('password')
    
        if not User.objects.filter(username=user_name).exists():
            messages.error(request,'invalid user name')
            return redirect('/login/')
        
        user=authenticate(username=user_name,password=password)
        if user is None:
           messages.error(request,"username/password did'nt matched")
           
        else:
            login(request,user)
            return redirect('/vege/')
             
        
        
    
    
    
    return render(request,'login.html')

@login_required(login_url="/login/")
def logout_handel(request):
    logout(request)
    
    return redirect('/login')




def get_students(request):
    queryset=Student.objects.all()
    
    #Pagination
    paginator = Paginator(queryset, 15)  # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    
    return render(request,'report/students.html',{'queryset':page_obj})
    
            
        
    
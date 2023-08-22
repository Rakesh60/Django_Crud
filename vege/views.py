from django.shortcuts import render,redirect,HttpResponse
from .models import *

# Create your views here.
def reciepies(request):
    if request.method=="POST":
        data=request.POST
        rec_image=request.FILES.get('reciepe_image')
        rec_name=data.get('reciepe_name')
        rec_desc=data.get('reciepe_description')
        
        
        Reciepe.objects.create(reciepe_name=rec_name,reciepe_description=rec_desc,reciepe_image=rec_image)
        
        return redirect('/vege/')
    
    
    
    queryset=Reciepe.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(reciepe_name__icontains=request.GET.get('search'))
    context={'reciepe':queryset}
    
        
       
    return render(request,'reciepe.html',context)


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
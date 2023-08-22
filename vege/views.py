from django.shortcuts import render,redirect
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
    context={'reciepe':queryset}
    
        
       
    return render(request,'reciepe.html',context)
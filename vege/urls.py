
from django.urls import path
from . import views

urlpatterns=[
     path('vege/',views.reciepies,name='reciepe'),
     path('delete/<rec_id>/',views.delete_reciepe,name='reciepe'),
     path('update/<rec_id>/',views.update_reciepe,name='reciepe'),
]

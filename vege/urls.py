
from django.urls import path
from . import views

urlpatterns = [
    path('vege/', views.reciepies, name='reciepe'),
    path('delete/<rec_id>/', views.delete_reciepe, name='reciepe'),
    path('update/<rec_id>/', views.update_reciepe, name='reciepe'),
    path('login/', views.login_handel, name='login'),
    path('', views.register_handel, name='register'),
    path('logout/', views.logout_handel, name='logout'),
    path('students/', views.get_students, name='get_studentss'),
    path('see_marks/<student_id>/', views.see_marks, name='see_marks'),


]

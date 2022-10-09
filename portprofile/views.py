from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        usermail=request.POST['email']
        print(usermail)
        name=request.POST['name']
        print(name)
        send_mail('Contact Form',f'Name: {name} \n \n Email: {usermail} \n \n Message: {message}', settings.EMAIL_HOST_USER, ['huzefataj8@gmail.com'], fail_silently=False)
    return render(request,'index.html')
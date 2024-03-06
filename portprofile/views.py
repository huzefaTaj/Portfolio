from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Project

# Create your views here.


def index(request):
    project = Project.objects.all()
    print(project)
    params = {'project': project}
    if request.method == 'POST':
        message = request.POST['message']
        usermail = request.POST['email']
        print(usermail)
        name = request.POST['name']
        print(name)
        send_mail('Portfolio Mail', f'Name: {name} \n \n Email: {usermail} \n \n Message: {message}', settings.EMAIL_HOST_USER, [
                  'huzefataj8@gmail.com'], fail_silently=False)
        return redirect(index)
    return render(request, 'index.html', params)

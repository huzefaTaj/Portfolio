from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Project,Seo

# Create your views here.


def index(request):
    seo=Seo.objects.get(id=1)
    cl=seo.clicks+1
    Seo.objects.filter(id=1).update(clicks=cl)
    
    



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

def cv(request):
    return render(request, 'cv.html')

from django.contrib import messages
from django.core.mail import message, send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from Appform.forms import StudentForm
from django.contrib import messages

# Create your views here.
def stdform(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'learning'
            message = 'Dear Candidate, \nWe are pleased to offer you an intership at our company'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient],fail_silently=False)
            messages.success(request, "Successfully Sent The Message!")
            return redirect('/')
    return render(request, 'home.html', {'form' : form})

   
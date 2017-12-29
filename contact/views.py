# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import contactForm

# Create your views here.
def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    context = {'title': title, 'form':form, }

    if form.is_valid():
        name =  form.cleaned_data['email']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE.com'
        message = '%s %s' %(comment,name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject,message,emailFrom,emailTo,fail_silently=True )
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you."
        context = {'title': title, 'confirm_message': confirm_message,}
    template = "contact.html"
    return render(request,template,context)


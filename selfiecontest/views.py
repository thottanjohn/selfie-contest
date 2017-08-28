# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect,render_to_response
from .forms import SignUpForm,ContactForm,EntryForm,GreenForm
from .models import Picto,userlike,Profile,GreenVibes
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from .forms import(
	ProfileForm,UserForm)
from django.contrib.auth.models import User
from django.http import Http404,HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect,JsonResponse
from django.db import transaction
from django.template import RequestContext

# Create your views here.
def home(request):
    title="welcome %s"%request.user
    return render(request,'index.html',context)
"""class EntryCreate(CreateView):
            model=Picto
            form_class=Picto
            template_name="entry.html"
            form_class.user=self.request.user
            form_class.save()
            fields=['image_caption','image']
class GreenEntryCreate(CreateView):
            model=GreenVibes
            template_name="greenentry.html"
            fields=['image_caption','image']"""
@login_required
def detail(request):
    title = "welcome %s" % request.user
    form = ContactForm(request.POST)
    if form.is_valid():
        form_mail = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'site contact form'
        from_email = form_mail
        to_email = [settings.EMAIL_HOST_USER, ]
        contact_message = form_message
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
    context = {
        'forms': form
    }
    pro=Picto.objects.all()
    for p in pro:
            p.liked = p.has_liked(request.user)
    return render(request,"hala.html",{'pro':pro,'forms':form})

def detail1(request):
    title = "welcome %s" % request.user
    form = ContactForm(request.POST)
    if form.is_valid():
        form_mail = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'site contact form'
        from_email = form_mail
        to_email = [settings.EMAIL_HOST_USER, ]
        contact_message = form_message
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
    context = {
        'forms': form
    }
    pro=GreenVibes.objects.all()
    for p in pro:
        p.liked = p.has_liked(request.user)
    return render(request,"hala.html",{'pro':pro,'forms':form})

@login_required
def gallery(request):
        pro=Picto.objects.all()
        for p in pro:
            p.liked = p.has_liked(request.user)
        return render(request, 'gallery.html',{'pro':pro})
def page(request):
    flag=0
    image_id=request.POST['image_id']
    us=Picto.objects.get(pk=image_id)
    users=userlike.objects.filter(image_id=image_id)
    if users.count() !=0:
        for user in users:
            if user.user==request.user:
                flag=1
                if user.favourite==True:
                    user.favourite=False
                    us.like-=1
                    us.save()
                    user.save()
                else:
                    user.favourite=True
                    us.like+=1
                    us.save()
                    user.save()
                break
        if flag!=1:
                user=userlike()
                user.image_id=image_id
                user.user=request.user
                us.like+=1
                us.save()
                user.favourite=True
                user.save()
    else:
        user=userlike()
        user.image_id=image_id
        user.user=request.user
        us.like+=1
        us.save()
        user.favourite=True
        user.save()
    if user.favourite:
        data={'like':us.like,'bol':1}
    else:
        data={'like':us.like,'bol':2}
    return JsonResponse(data)
def events(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form_mail = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'site contact form'
        from_email = form_mail
        to_email = [settings.EMAIL_HOST_USER, ]
        contact_message = "Hello %s,Welcome to new era" % form_full_name
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
    context = {
        'forms': form
    }
    return render(request,"events.html",context)
@login_required
def view_profile(request):
	args={'user':request.user}
	return render(request, 'profile.html', args)
	
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
def about(request):
    title = "welcome %s" % request.user
    form = ContactForm(request.POST)
    if form.is_valid():
        form_mail = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'site contact form'
        from_email = form_mail
        to_email = [settings.EMAIL_HOST_USER, ]
        contact_message =form_message
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
    context = {
        'forms': form
    }
    return render(request,"about1.html",context)
@login_required
@transaction.atomic
def EntryCreate(request):
    if request.method == 'POST':
        user_form = EntryForm(request.POST,request.FILES)
        user_form.user=request.user
        if user_form.is_valid():
            user_form.save()
            return redirect('home')
    else:
        user_form = EntryForm()
    return render(request, 'entry.html', {
        'form': user_form
    })
@login_required
@transaction.atomic
def GreenEntryCreate(request):
    if request.method == 'POST':
        user_form = GreenForm(request.POST,request.FILES)
        user_form.user=request.user
        if user_form.is_valid():
            user_form.save()
            return redirect('home')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = GreenForm()
    return render(request, 'greenentry.html', {
        'form': user_form
    })
@login_required
def alt_profile(request,profile_id):
    	try:
            user = User.objects.get(username=profile_id)
            args={'user':user}
        except:
            raise Http404
        return render(request, 'altprofile.html', args)
@login_required
def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form_mail = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'site contact form'
        from_email = form_mail
        to_email = [settings.EMAIL_HOST_USER, ]
        contact_message = "Hello %s,Welcome to new era" % form_full_name
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
    context = {
        'forms': form
    }
    return render(request, 'contact.html',context)
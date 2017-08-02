# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SignUp,Picto,userlike,Profile

class SignUpAdmin(admin.ModelAdmin):
    list_display=["__unicode__","timestamp","updated"]
    class Meta:
        model= SignUp

admin.site.register(SignUp,SignUpAdmin)
admin.site.register(Picto)
admin.site.register(userlike)
admin.site.register(Profile)
# Register your models here.

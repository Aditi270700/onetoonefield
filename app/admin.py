from django.contrib import admin

# Register your models here.
from .models import Aadhar
from .models import userProfile


admin.site.register(Aadhar)
admin.site.register(userProfile)
from django.contrib import admin
from .models import Make, Auto

# Register your models here.
admin.site.register([Make, Auto])

from django.contrib import admin
from .models import Breed, Cat

admin.site.register([Breed, Cat])

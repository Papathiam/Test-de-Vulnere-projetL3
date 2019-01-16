from django.contrib import admin

# Register your models here.
from .models import NmapScan

admin.site.register(NmapScan)
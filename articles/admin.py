from django.contrib import admin
from articles.models import Articles,NmapScan ,Comment
# Register your models here.
admin.site.register(Articles)

admin.site.register(NmapScan)

admin.site.register(Comment)



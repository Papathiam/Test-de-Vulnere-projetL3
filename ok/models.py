from django.db import models

# Create your models here.
class NmapScan(models.Model):
    target = models.CharField(max_length=2048)

    def _str__(self):
        return self.target
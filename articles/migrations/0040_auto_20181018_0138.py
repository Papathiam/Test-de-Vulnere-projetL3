# Generated by Django 2.1.2 on 2018-10-18 01:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0039_auto_20181018_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='articles',
            field=models.ForeignKey(on_delete=True, related_name='comments', to='articles.Articles'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(on_delete=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

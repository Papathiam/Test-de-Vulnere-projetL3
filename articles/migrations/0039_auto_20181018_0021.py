# Generated by Django 2.1.2 on 2018-10-18 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0038_auto_20181017_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='articles',
            field=models.ForeignKey(on_delete=True, related_name='comments', to='articles.Articles'),
        ),
    ]

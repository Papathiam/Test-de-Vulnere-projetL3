# Generated by Django 2.1.2 on 2018-10-17 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0035_auto_20181017_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='articles',
            field=models.ForeignKey(on_delete=True, related_name='comments', to='articles.Articles'),
        ),
    ]

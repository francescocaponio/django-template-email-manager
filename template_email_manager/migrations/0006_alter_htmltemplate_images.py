# Generated by Django 3.2 on 2021-04-27 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_email_manager', '0005_auto_20210426_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmltemplate',
            name='images',
            field=models.ManyToManyField(blank=True, to='template_email_manager.ImageAttachment'),
        ),
    ]

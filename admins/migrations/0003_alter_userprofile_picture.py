# Generated by Django 4.1.4 on 2023-01-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_alter_userprofile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/avatar'),
        ),
    ]

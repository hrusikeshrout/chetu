# Generated by Django 2.1.5 on 2022-01-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]

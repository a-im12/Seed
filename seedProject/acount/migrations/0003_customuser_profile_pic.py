# Generated by Django 4.1 on 2023-04-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acount', '0002_customuser_is_general_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-14 15:58

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('dsapp', '0002_babylion'),
    ]

    operations = [
        migrations.CreateModel(
            name='failure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('phone_num', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
    ]

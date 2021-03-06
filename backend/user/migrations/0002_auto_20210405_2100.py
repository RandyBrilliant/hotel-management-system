# Generated by Django 3.1.7 on 2021-04-05 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Joined'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Login'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('gender', models.CharField(choices=[('MA', 'Male'), ('FE', 'Female'), ('OT', 'Other')], max_length=2, verbose_name='Gender')),
                ('id_proof', models.CharField(max_length=200, verbose_name='ID Proof')),
                ('address_proof', models.CharField(max_length=200, verbose_name='Address Proof')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='Profile Picture')),
                ('status', models.CharField(max_length=200)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

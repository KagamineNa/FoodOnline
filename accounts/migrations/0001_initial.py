# Generated by Django 4.2.6 on 2023-10-10 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Restaurant'), (2, 'Customer')], null=True)),
                ('date_joinded', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/profiles_pictures')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='users/cover_photos')),
                ('address_line_1', models.CharField(blank=True, max_length=50, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=15, null=True)),
                ('state', models.CharField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=6, null=True)),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

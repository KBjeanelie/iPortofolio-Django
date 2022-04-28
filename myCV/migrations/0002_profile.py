# Generated by Django 4.0.4 on 2022-04-28 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myCV', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_profile', models.ImageField(upload_to='profile_pics/')),
                ('birthday', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=100)),
                ('available', models.BooleanField(default=False)),
                ('status_job_one', models.CharField(max_length=100)),
                ('status_job_two', models.CharField(max_length=100)),
                ('bio', models.CharField(help_text='Short Bio (eg. I love cats and games)', max_length=100)),
                ('address', models.CharField(help_text='Enter Your Address', max_length=100)),
                ('city', models.CharField(help_text='Enter Your City', max_length=100)),
                ('country', models.CharField(help_text='Enter Your Country', max_length=100)),
                ('twitter_url', models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('instagram_url', models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('facebook_url', models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('github_url', models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('website_url', models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.1.7 on 2022-07-30 15:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegisteredVoters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=250)),
                ('profile', models.ImageField(upload_to='onlinevote/uploads/profile')),
                ('matric', models.CharField(max_length=50, unique=True)),
                ('verified_voter', models.BooleanField(default=False)),
                ('aspirant', models.BooleanField(default=False)),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_school', to='accounts.department')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='year_year', to='accounts.year')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='department',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_depart', to='accounts.school'),
        ),
    ]
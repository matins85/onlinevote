# Generated by Django 3.1.7 on 2022-08-25 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_registeredvoters_verified_aspirant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredvoters',
            name='profile',
            field=models.TextField(),
        ),
    ]

# Generated by Django 3.1.7 on 2022-07-31 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220730_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredvoters',
            name='profile',
            field=models.ImageField(upload_to='onlinevote/voters'),
        ),
        migrations.AlterField(
            model_name='registeredvoters',
            name='verified_voter',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='AspirantPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=250)),
                ('position_type', models.CharField(choices=[('sug', 'SUG'), ('department', 'DEPARTMENT')], max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aspirant_depart', to='accounts.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='registeredvoters',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='voter_position', to='accounts.aspirantposition'),
        ),
    ]

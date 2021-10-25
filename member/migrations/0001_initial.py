# Generated by Django 2.2.4 on 2019-08-13 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=20, unique=True, verbose_name='ID')),
                ('is_trainee', models.BooleanField(default=True, verbose_name='Trainee')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Adm')),
                ('hour_week', models.DurationField(default='0', verbose_name='Relatório Semanal')),
                ('total_hour', models.DurationField(default='0', verbose_name='Relatório Geral')),
                ('created_password', models.BooleanField(default=False, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Membro')),
            ],
            options={
                'verbose_name': 'Membro',
                'verbose_name_plural': 'Membros',
            },
        ),
    ]
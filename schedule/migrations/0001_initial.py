# Generated by Django 2.2.4 on 2019-08-13 19:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_week', models.IntegerField(choices=[(1, 'Segunda-feira'), (2, 'Terça-feira'), (3, 'Quarta-feira'), (4, 'Quinta-feira'), (5, 'Sexta-feira')], verbose_name='Dia da Semana')),
                ('hour_beg', models.TimeField(default=django.utils.timezone.now, verbose_name='Hora início')),
                ('hour_end', models.TimeField(default=django.utils.timezone.now, verbose_name='Hora fim')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member', verbose_name='Membro')),
            ],
            options={
                'verbose_name': 'Horário',
                'verbose_name_plural': 'Horários',
            },
        ),
    ]

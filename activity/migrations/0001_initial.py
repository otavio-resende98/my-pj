# Generated by Django 2.2.4 on 2019-08-13 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour_beg', models.DateTimeField(verbose_name='Hora início')),
                ('hour_end', models.DateTimeField(blank=True, null=True, verbose_name='Hora fim')),
                ('is_rg', models.BooleanField(default=False, verbose_name='Reunião Geral (RG)')),
                ('is_extra', models.BooleanField(default=False, verbose_name='Atividade Extra')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member', verbose_name='Membro')),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
            },
        ),
    ]

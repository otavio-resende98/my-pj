import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Membro",
    )
    card_id = models.CharField("ID", max_length=20, unique=True)
    is_trainee = models.BooleanField("Trainee", default=True)
    is_admin = models.BooleanField("Adm", default=False)
    hour_week = models.DurationField("Relatório Semanal", default='0')
    total_hour = models.DurationField("Relatório Geral", default='0')
    created_password = models.BooleanField(default=False, editable=False)

    def password_was_created(self):
        return self.created_password

    def get_total_hours(self):
        hours, _ = self.total_hour.total_seconds()/3600
        return hours

    def get_week_hours(self):
       hours, remainder = divmod(self.hour_week.seconds, 3600)
       minutes, _ = divmod(remainder,60)
       return hours, minutes

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"

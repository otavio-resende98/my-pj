from django.utils.timezone import now
from django.db import models

from member.models import Member
from .choices import DAYWEEK_CHOICES

class Schedule(models.Model):
    day_week = models.IntegerField("Dia da Semana", choices=DAYWEEK_CHOICES)
    hour_beg = models.TimeField("Hora início", default=now)
    hour_end = models.TimeField("Hora fim", default=now)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="Membro")

    def prettify_time(self, time):
       hours, remainder = divmod(time.seconds, 3600)
       minutes, _ = divmod(remainder,60)
       return "{}:{}".format(hours, minutes)

    def __str__(self):
        return "{} - {}:{}~{}:{} [{}]".format(self.member,
                                         self.hour_beg.hour,
                                         self.hour_beg.minute,
                                         self.hour_end.hour,
                                         self.hour_end.minute,
                                         self.get_day_week_display())


    class Meta:
        verbose_name = "Horário"
        verbose_name_plural = "Horários"

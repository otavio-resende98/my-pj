import datetime
from django.db import models
from member.models import Member


class Activity(models.Model):
    hour_beg = models.DateTimeField("Hora início")
    hour_end = models.DateTimeField("Hora fim", blank=True, null=True)
    is_rg = models.BooleanField("Reunião Geral (RG)", default=False)
    is_extra = models.BooleanField("Atividade Extra", default=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="Membro")

    def prettify_date(self, date):
       return "{}/{}".format(date.day, date.month)

    def __str__(self):
        return "{} - {}".format(self.member, self.prettify_date(self.hour_beg))
                

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"

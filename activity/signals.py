from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Activity
from .tasks import check_for_missed_outs_task

@receiver(post_save, sender=Activity)
def check_for_end(instance, created, **kwargs): 
    if created:
        check_for_missed_outs_task.delay(instance.id)

import datetime

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User

from member.models import Member
from activity.models import Activity

@receiver(post_save, sender=Activity)
def update_member_hours(instance, created, **kwargs):
    """ Atualiza horas de membro ao realizar o fechamento de um ponto """    
    if not created:
        member = Member.objects.filter(pk=instance.member.id).first()        
        member.total_hour += instance.hour_end - instance.hour_beg
        member.hour_week += instance.hour_end - instance.hour_beg

        # Limite de 4 horas semanais
        if member.hour_week > datetime.timedelta(hours=4):
            member.hour_week = datetime.timedelta(hours=4)

        member.save()

@receiver(pre_save, sender=User)
def user_updated(instance, **kwargs):
    """ Ao atualizar a senha, não será mais mostrado o form de alteração de 
    senha ao se logar """
    user = instance
    if user:
        new_password = user.password
        try:
            old_password = User.objects.get(pk=user.pk).password
        except User.DoesNotExist:
            return
        if new_password != old_password:
            member = Member.objects.filter(user=user).first()

            if not member.password_was_created():
                member.created_password = True
                member.save()

#TODO: find a better place to place this `User` stuff
@receiver(post_save, sender=Member)
def member_updated(instance, created, **kwargs):
    """ Atualiza um membro para admin """
    if not created:
        member = instance
        user = member.user 
        if member.is_admin and not user.is_staff:
            user.is_staff = True
            user.is_superuser = True
        elif not member.is_admin and user.is_staff:
            user.is_staff = False
            user.is_superuser = False
        else:
            return
        user.save()


import json
import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from member.models import Member
from .models import Activity
from Ponto_Juridico.settings import (BUSINESS_RG_BEG_HOUR,
                                  BUSINESS_RG_BEG_MINUTE,
                                  BUSINESS_RG_END_HOUR,
                                  BUSINESS_RG_END_MINUTE,
                                  BUSINESS_RG_WEEK_DAY,)

@require_POST
@csrf_exempt
def new_activity(request):
    # Novo ponto de entrada
    def new_entry(entry):
        member = Member.objects.filter(card_id=entry["id"]).first()
        activity = Activity()
        weekday = activity_time.isoweekday()
        hour = activity_time.hour

        activity.hour_beg = activity_time
        activity.hour_end = None
        activity.is_rg = False
        activity.is_extra = False
        activity.member = member

        if (weekday == 3 and hour in range(BUSINESS_RG_BEG_HOUR,
                BUSINESS_RG_END_HOUR) and minute in range(0,
                BUSINESS_RG_END_MINUTE)):
                              
            print("é RG")
            activity.is_rg = True

        elif weekday in range(1, 6):
            print("é dia da semana", )

        '''
        else:
            print("não é dia da semana")
            activity.is_extra = True
        '''

        try:
            activity.save()
        except:
            return "failed"

        return "success"

    # Novo ponto de saída
    def new_out(out):
        activity = Activity.objects.filter(member__card_id=out["id"]).last()

        # Ponto de entrada ainda não foi fechado
        if activity.hour_end is None:
            activity.hour_end = activity_time
            activity.save()

            return "success"

        return "failed"

    activity = json.loads(request.body)
    activity_time = datetime.datetime.strptime(activity["time"],
                                               '%Y-%m-%d %H:%M:%S')

    if activity["type"]:
        status = new_entry(activity)
    else:
        status = new_out(activity)

    response = {
            "status": status,
            }

    return HttpResponse(json.dumps(response), content_type="application/json")


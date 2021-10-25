import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Member

@login_required
def home(request):
    user = request.user
    member = Member.objects.filter(user=user).first()
    if member.password_was_created():
        print('aaa')
        hours, minutes = member.get_week_hours()
        context = {
            "user": user,
            "hours": hours,
            "minutes": minutes,
        }
        return render(request, 'member/home.html', context=context)
    else:
        return render(request, 'account/password_change.html', context={})

@require_POST
@csrf_exempt
def new_member(request):
    # Cadastrar membro (name, email e card_id)
    new_member = Member()
    activity = json.loads(request.body)
    try:
        user = User.objects.create_user(
                     username=activity["name"],
                     first_name=activity["name"][:activity["name"].find(" ")],
                     last_name=activity["name"][activity["name"].find(" ") + 1:],
                     email=activity["email"],
                     password='juridica123')
        new_member.user = user
        new_member.card_id = activity["id"]
        new_member.save()
        status = True
    except:
        status = False

    response = {
        "status": status
    }

    return HttpResponse(json.dumps(response), content_type="application/json")

from django.contrib import admin
from .models import Schedule
from .choices import DAYWEEK_CHOICES


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):

    search_fields = ['^member__user__first_name']

    # search by week_day
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request,
                                                            queryset,
                                                            search_term)
        days = {v.lower(): k for k, v in DAYWEEK_CHOICES}
        try:
            day = days[search_term.lower()]
        except KeyError:
            pass
        else:
            queryset |= self.model.objects.filter(day_week=day)
        return queryset, use_distinct

    def get_queryset(self, request):
        return Schedule.objects.order_by('day_week', 'hour_beg')


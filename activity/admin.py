from django.contrib import admin
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    readonly_fields = ["hour_beg", "hour_end"]

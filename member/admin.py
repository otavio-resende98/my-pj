from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ["card_id", "user"]

    def has_add_permission(self, request, obj=None):
        return False

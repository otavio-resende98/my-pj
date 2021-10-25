from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site

admin.site.site_header = "Administração Jurídica Jr."
admin.site.site_title = "Jurídica Jr."
admin.site.index_title = "Administração de horários"

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(Site)

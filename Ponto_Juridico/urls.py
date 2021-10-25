from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.conf.urls import handler500, handler404

# handler404 =  'core.views.handler404'
# handler500 =  'core.views.handler500'

urlpatterns = [
    path("", include('member.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path("activity/", include('activity.urls')),
    path("mail/", include('mail.urls')),
    # Django Admin, use {% url 'admin:index' %}
    # path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('session_security/', include('session_security.urls')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('_debug_/', include(debug_toolbar.urls)),
    ]
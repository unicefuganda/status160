from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from rapidsms_httprouter.urls import urlpatterns as router_urls
from tracking.urls import urlpatterns as tracking_urls
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^my-project/', include('my_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    
    # RapidSMS core URLs
    (r'^account/', include('rapidsms.urls.login_logout')),
    url(r'^$', 'status160.views.index', name='rapidsms-dashboard'),
    url('^accounts/login', 'rapidsms.views.login'),
    url('^accounts/logout', 'rapidsms.views.logout'),
    # RapidSMS contrib app URLs
    (r'^ajax/', include('rapidsms.contrib.ajax.urls')),
#    (r'^export/', include('rapidsms.contrib.export.urls')),
    (r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    (r'^locations/', include('rapidsms.contrib.locations.urls')),
    (r'^messagelog/', include('rapidsms.contrib.messagelog.urls')),
    (r'^messaging/', include('rapidsms.contrib.messaging.urls')),
    (r'^registration/', include('auth.urls')),
    (r'^scheduler/', include('rapidsms.contrib.scheduler.urls')),
    (r'^status160/', include('status160.urls')),
    (r'^polls/', include('poll.urls')),
    (r'^supply/', include('supplytracking.urls')),
) + router_urls + tracking_urls

if settings.DEBUG:
    urlpatterns += patterns('',
        # helper URLs file that automatically serves the 'static' folder in
        # INSTALLED_APPS via the Django static media server (NOT for use in
        # production)
        (r'^', include('rapidsms.urls.static_media')),
    )

from rapidsms_httprouter.router import get_router
get_router(start_workers=True)



from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from <%= packagename %>.dashboard.app import application as <%= packagename %>_dashboard
from oscar.app import application

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(application.urls)),
    url(r'^dashboard/<%= packagename %>/', include(<%= packagename %>_dashboard.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += staticfiles_urlpatterns()
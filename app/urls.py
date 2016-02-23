# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
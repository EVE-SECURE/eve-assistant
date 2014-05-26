from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'eve.views.home', name='home'),
    url(r'^$', include('calc.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

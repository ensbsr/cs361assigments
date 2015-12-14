from django.conf.urls import patterns, include, url
import views
from hw1.views import word_frequency

from django.contrib import admin


urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)),

    url(r'^histogram/(?P<file>.*)$', word_frequency),

)

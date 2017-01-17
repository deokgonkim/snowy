#
# Copyright (c) 2009 Brad Taylor <brad@getcoded.net>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.views.generic.simple import direct_to_template, redirect_to
from django.core.urlresolvers import reverse
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

handler500 = 'snowy.views.server_error'

urlpatterns = patterns('',
    url(r'^notes/$', direct_to_template, {'template': 'index.html'},
        name='snowy_index'),

    (r'^notes/api/', include('snowy.api.urls')),
    (r'^notes/accounts/', include('snowy.accounts.urls')),
    (r'^notes/admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^notes/admin/', include(admin.site.urls)),

    (r'^notes/export/', include('snowy.export.urls')),

    (r'^notes/mobile/', include('snowy.mobile_notes.urls')),

    url(r'^notes/(?P<username>\w+)/$', 'snowy.views.user_index', name="user_index"),
    (r'^notes/(?P<username>\w+)/notes/', include('snowy.notes.urls')),
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^notes/site_media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }))

# OAuth
urlpatterns += patterns('piston.authentication',
    url(r'^notes/oauth/request_token/$', 'oauth_request_token', name='oauth_request_token'),
    url(r'^notes/oauth/authenticate/$', 'oauth_user_auth', name='oauth_user_auth'),
    url(r'^notes/oauth/access_token/$', 'oauth_access_token', name='oauth_access_token'),
)

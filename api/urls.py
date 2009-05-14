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

from django.conf.urls.defaults import *

from piston.resource import Resource
from snowy.api.handlers import UserHandler

user_handler = Resource(UserHandler)

urlpatterns = patterns('',
    url(r'(?P<username>\w+)/$', user_handler),
#    url(r'^(?P<username>\w+)/notes$', note_handler),
#    url(r'^(?P<username>\w+)/notes$', note_handler),
)
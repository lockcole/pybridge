# PyBridge -- online contract bridge made easy.
# Copyright (C) 2004-2006 PyBridge Project.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.


from ConfigParser import SafeConfigParser

from pybridge.conf import TCP_PORT
from pybridge.environment import CLIENT_SETTINGS_PATH


settings = SafeConfigParser()
settings.read([CLIENT_SETTINGS_PATH])

# Create sections and options, if they do not exist.

if not settings.has_section('connection'):
	settings.add_section('connection')
	settings.set('connection', 'hostname', '')
	settings.set('connection', 'portnum', str(TCP_PORT))
	settings.set('connection', 'username', '')
	settings.set('connection', 'password', '')
	settings.write(file(CLIENT_SETTINGS_PATH, 'w'))


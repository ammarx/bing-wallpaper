#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of bing-background
#
# Copyright (C) 2017
# Ammar Ahmad <ammar.ahmad1993@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import locale
import gettext
import sys

__author__ = 'Ammar Ahmad <ammar.ahmad1993@gmail.com>'
__copyright__ = 'Copyright (c) 2017 Ammar Ahmad'
__license__ = 'GPLV3'
__url__ = 'https://www.github.com/ammarx'
__version__ = '0.1.0'

######################################


def is_package():
    return __file__.find('src') < 0

######################################


VERSION = __version__
APP = 'bing-wallpaper'
APPNAME = APP
APP_CONF = APP + '.conf'
CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.config')
CONFIG_APP_DIR = os.path.join(CONFIG_DIR, APP)
POTD = os.path.join(CONFIG_APP_DIR, 'potd.jpg')
# check if running from source
if is_package():
    ROOTDIR = os.path.join('/opt/extras.ubuntu.com/', APP)
    APPDIR = os.path.join(ROOTDIR, 'share', APP)
    DICTSDIR = os.path.join(APPDIR, 'dicts')
    LANGDIR = os.path.join(ROOTDIR, 'locale-langpack')
    ICONDIR = os.path.join(ROOTDIR, 'share/icons')
    BD = os.path.join(APPDIR, 'bdownloader.py')
    AUTOSTART = os.path.join(APPDIR,
                             'bing-wallpaper-autostart.desktop')
else:
    VERSION = VERSION + '-src'
    ROOTDIR = os.path.dirname(__file__)
    LANGDIR = os.path.normpath(os.path.join(ROOTDIR, '../template1'))
    APPDIR = ROOTDIR
    ICONDIR = os.path.normpath(os.path.join(ROOTDIR, '../data'))
    BD = os.path.join(APPDIR, 'bdownloader.py')
    AUTOSTART = os.path.join(APPDIR,
                             'bing-wallpaper-autostart.desktop')

#
ICON = os.path.join(ICONDIR, APP + '.svg')

try:
    current_locale, encoding = locale.getdefaultlocale()
    language = gettext.translation(APP, LANGDIR, [current_locale])
    language.install()
    if sys.version_info[0] == 3:
        _ = language.gettext
    else:
        _ = language.ugettext
except Exception as e:
    print(e)
    _ = str

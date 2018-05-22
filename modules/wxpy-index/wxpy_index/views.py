# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2018 QiaoPeng.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.

"""weixin program develop."""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from __future__ import absolute_import, print_function

from flask import Blueprint, jsonify, render_template, request, url_for
from flask_babelex import gettext as _

blueprint = Blueprint(
    'wxpy_index',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/wxpy',
)

blueprint_rest = Blueprint(
    'wxpy_index_api',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@blueprint.route('/')
@blueprint.route('/index')
def index():
    """Render a basic view."""
    return render_template(
        'wxpy_index/index.html',
        module_name=_('Wxpy-Index'))


@blueprint_rest.route('/test')
def test_api():
    """Return a basic json.

    access uri: /api/test
    """
    return jsonify({'code': 0, 'msg': _('success'), 'data': {'uri': url_for('wxpy_index_api.test_api'), 'method': request.method}})

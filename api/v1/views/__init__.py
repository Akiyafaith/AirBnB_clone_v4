#!/usr/bin/python3
"""importBlueprint"""

from flask import Blueprint
"""create a variable with an instance Blueprint"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

import api.v1.views.index
import api.v1.views.states
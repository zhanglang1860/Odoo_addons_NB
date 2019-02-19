# -*- coding: utf-8 -*-
import sys
from . import autoproject, autowind, autocivil, autoeconomic, autoelectrical
parentUrl=r'C:\Program Files (x86)\Odoo 12.0\server\odoo'
sys.path.append(parentUrl)
print(sys.path)
import models, fields, api
from django.contrib import admin
from . import models

# Register all models for quick CRUD in Admin
for name in dir(models):
    obj = getattr(models, name)
    try:
        if getattr(obj, '_meta', None) and getattr(obj._meta, 'abstract', False) is False:
            admin.site.register(obj)
    except admin.sites.AlreadyRegistered:
        pass

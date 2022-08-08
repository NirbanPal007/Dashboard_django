from django.contrib import admin
from dboardo.models import Component, ComponentType, Report, Topic

# Register your models here.
admin.site.register(Topic)
admin.site.register(Report)
admin.site.register(ComponentType)
admin.site.register(Component)



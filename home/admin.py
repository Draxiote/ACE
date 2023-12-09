from django.contrib import admin
from home.models import Contact, Credentials, Forum, Event, Alert

# Register your models here.
admin.site.register(Contact)
admin.site.register(Credentials)
admin.site.register(Forum)
admin.site.register(Event)
admin.site.register(Alert)
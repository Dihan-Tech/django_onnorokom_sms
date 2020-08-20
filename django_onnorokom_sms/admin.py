from django.contrib import admin
from .models import DjangoOnnorokomSMSModel


# Register your models here.
class DjangoOnnorokomSMSModelAdmin(admin.ModelAdmin):
    list_display = ['message_text', 'sent_by', 'sent_to', 'is_active', 'is_success', 'sms_time']
    search_fields = ['sent_by__pk', 'sent_to']

    def sms_time(self, obj):
        return str(obj.get_timesince()) + ' ago'


admin.site.register(DjangoOnnorokomSMSModel, DjangoOnnorokomSMSModelAdmin)

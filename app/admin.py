from django.contrib import admin
from .models import *
from .forms import *

@admin.register(QRcode)
class QRcodeAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'timestamp', 'validitytime', 'endtime', 'creator', 'data')
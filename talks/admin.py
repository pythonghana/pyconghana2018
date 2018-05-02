from django.contrib import admin
from .models import Proposal


class TalkAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "talk_type", "intended_audience", "status")
    list_editable = ["status"]
    list_filter = ("talk_type", "status")

admin.site.register(Proposal, TalkAdmin)
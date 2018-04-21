from django.contrib import admin
from .models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    list_display = ("sponsor_name", "category", "type")
    list_filter = ["category", "type"]


admin.site.register(Sponsor, SponsorAdmin)

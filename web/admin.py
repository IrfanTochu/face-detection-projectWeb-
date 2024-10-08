from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'language', 'visit_count', 'last_visit')
    list_filter = ('language',)
    search_fields = ('ip_address',)
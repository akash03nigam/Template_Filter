from django.contrib import admin
from testapp.models import Filter
# Register your models here.
class FilterAdmin(admin.ModelAdmin):
    list_display=['Name', 'Email', 'Date']

admin.site.register(Filter,FilterAdmin)
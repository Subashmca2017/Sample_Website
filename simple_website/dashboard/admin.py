from django.contrib import admin
from django.contrib.auth.models import Group
from .models import AssestsConfig

# Register your models here.
admin.site.unregister(Group)

admin.site.site_header = "Config Dashboard Images"


class CongigRegister(admin.ModelAdmin):
    list_display = ('preview_images',)


admin.site.register(AssestsConfig, CongigRegister)

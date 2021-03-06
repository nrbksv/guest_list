from django.contrib import admin

from check_in.models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'name', 'e_mail', 'create_date', 'update_date']
    list_filter = ['status']
    search_fields = ['status', 'name']
    fields = ['id', 'status', 'name', 'e_mail', 'reg_info', 'create_date', 'update_date']
    readonly_fields = ['id', 'create_date', 'update_date']


admin.site.register(Guest, GuestAdmin)


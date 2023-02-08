from django.contrib import admin

from home.models import Contact, Gender, BloodGroup, Index_bgs, DyfiUnit

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','Name','email','message','contact_date')
    def has_add_permission(self, request, obj = None):
        return False
admin.site.register(Contact, ContactAdmin)


class GenderAdmin(admin.ModelAdmin):
    list_display=('id', 'gender')
    def has_add_permission(self, request, obj = None):
        return False
admin.site.register(Gender, GenderAdmin)

class BloodGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'b_group')
    def has_add_permission(self, request, obj = None):
        return False
admin.site.register(BloodGroup, BloodGroupAdmin)

class IndexAdmins(admin.ModelAdmin):
    list_display=('b_name','b_fathers_name', 'b_group', 'b_gender', 'b_donated')
admin.site.register(Index_bgs, IndexAdmins)

class DyfiUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit')
admin.site.register(DyfiUnit, DyfiUnitAdmin)

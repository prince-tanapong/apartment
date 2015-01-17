from django.contrib import admin
from records.models import Renter


# Register your models here.
class RenterAdmin(admin.ModelAdmin):
    ordering = ['first_name']
    list_display = ('__unicode__', 'telephon_number', 'move_in_date')

admin.site.register(Renter, RenterAdmin)

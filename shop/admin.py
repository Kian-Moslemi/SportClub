from django.contrib import admin
from .models import TimeSlot,Service,Booking,FeadBack

admin.site.register(TimeSlot)
admin.site.register(Service)
admin.site.register(FeadBack)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    ordering = ('-timeslot',)
    readonly_fields = ('created_at',)

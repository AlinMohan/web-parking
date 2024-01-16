from django.contrib import admin
from app1.models import Users,Staff,ParkingSlot,BookedSlot
# Register your models here.

admin.site.site_header = 'ParkAssist Administrator Homepage'
class UsersAdmin(admin.ModelAdmin):
    list_display = ('Name','Phone','Email','VehicleNumber','Username','Password')

admin.site.register(Users,UsersAdmin)

admin.site.register(Staff)

admin.site.register(ParkingSlot)

admin.site.register(BookedSlot)




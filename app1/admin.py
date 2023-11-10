from django.contrib import admin
from app1.models import Users,Staff
# Register your models here.
admin.site.site_header = 'ParkAssist Administrator Homepage'
class UsersAdmin(admin.ModelAdmin):
    list_display = ('UserId','Name','Phone','Email','VehicleNumber','Username','Password')

admin.site.register(Users,UsersAdmin)

admin.site.register(Staff)




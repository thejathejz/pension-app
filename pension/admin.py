from django.contrib import admin
from .models import UserAccountDetails,Profile, ServiceStatus,BookAppointment
from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.

admin.site.unregister(User)
admin.site.register(Profile)
admin.site.register( ServiceStatus)
admin.site.register( BookAppointment)
@admin.register(UserAccountDetails)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','phone_number','otp']
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'id')
    readonly_fields = ('id',)

admin.site.register(User, CustomUserAdmin)

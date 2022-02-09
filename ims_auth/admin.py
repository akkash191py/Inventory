from django.contrib import admin
from .models import User, Profile, Address

# Register UserAdmin models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'role', 'profile_pic', 'date_joined')
admin.site.register(User, UserAdmin)

# Register ProfileAdmin models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'address', 'role', 'date_of_joining')
admin.site.register(Profile, ProfileAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'addresses', 'street', 'city', 'state', 'country', 'postcode')
admin.site.register(Address, AddressAdmin)

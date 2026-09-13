from django.contrib import admin

from products.admin import BasketAdmin
from users.models import EmailVerification, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    inlines = [BasketAdmin]


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration', 'get_is_verified')

    @admin.display(description='Подтвержден', boolean=True)
    def get_is_verified(self, obj):
        return obj.user.is_verified_email

    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)

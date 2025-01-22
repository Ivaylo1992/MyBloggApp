from django.contrib import admin

from simpleblog.accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...

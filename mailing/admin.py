from django.contrib import admin

from mailing.models import Client, Mailing, Message, MailingAttempts


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'email')


@admin.register(Mailing)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('message', 'regularity', 'status')


@admin.register(Message)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('subject',)


@admin.register(MailingAttempts)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('mailing',)

from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'created_at', 'subscribed_totay')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')

    def subscribed_totay(self, obj):
        return obj.created_at.date() == now().date()

    subscribed_totay.short_description = 'inscrito hoje?'
    subscribed_totay.boolean = True


admin.site.register(Subscription, SubscriptionAdmin)


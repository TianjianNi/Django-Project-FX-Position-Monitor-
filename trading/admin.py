from django.contrib import admin
from .models import Trade

class TradeAdmin(admin.ModelAdmin):
    list_display = ("id", "currency", "buy_sell", "amount")

# Register your models here.
admin.site.register(Trade, TradeAdmin)
from django.contrib import admin
from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from zoneinfo import ZoneInfo
import pprint
from .models import *

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'created_date_ubb', 'total_items', 'total_price')
    readonly_fields = ('cart_id', 'created_date_ubb')

    def created_date_ubb(self, obj):
        # Convert UTC created_date to Ulaanbaatar timezone
        ulaanbaatar_tz = ZoneInfo("Asia/Ulaanbaatar")
        return obj.created_date.astimezone(ulaanbaatar_tz).strftime("%Y-%m-%d %H:%M:%S")
    created_date_ubb.short_description = "Created Date (UB Time)"

    def total_items(self, obj):
        return sum(item.quantity for item in obj.cartitem_set.all())
    total_items.short_description = "Total Items"

    def total_price(self, obj):
        return sum(item.sub_total() for item in obj.cartitem_set.all())
    total_price.short_description = "Total Price"
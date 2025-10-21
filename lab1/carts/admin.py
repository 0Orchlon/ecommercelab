from django.contrib import admin
from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from zoneinfo import ZoneInfo
import pprint
from .models import *

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'get_created_date_ub', 'expire_date', 'get_decoded_data')
    readonly_fields = ('session_key', 'expire_date', 'get_decoded_data')
    ordering = ('-expire_date',)  # ✅ newest sessions first (consistent sorting)

    def get_created_date_ub(self, obj):
        """
        Estimate created date = expire_date - SESSION_COOKIE_AGE,
        convert to Asia/Ulaanbaatar timezone and format nicely.
        """
        session_age = getattr(settings, 'SESSION_COOKIE_AGE', 1209600)  # default 2 weeks
        created = obj.expire_date - timedelta(seconds=session_age)

        # Make sure it's timezone-aware
        if timezone.is_naive(created):
            created = timezone.make_aware(created, timezone=timezone.utc)

        # Convert to Ulaanbaatar timezone
        ub_tz = ZoneInfo("Asia/Ulaanbaatar")
        created_ub = created.astimezone(ub_tz)

        return created_ub.strftime("%Y-%m-%d %H:%M:%S %Z")

    get_created_date_ub.short_description = 'Created (Ulaanbaatar)'

    def get_decoded_data(self, obj):
        try:
            return pprint.pformat(obj.get_decoded())
        except Exception:
            return "Invalid or corrupted session"
    get_decoded_data.short_description = "Session Data"

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'created_date', 'total_items', 'total_price')
    readonly_fields = ('cart_id', 'created_date')

    def total_items(self, obj):
        return sum(item.quantity for item in obj.cartitem_set.all())
    total_items.short_description = "Total Items"

    def total_price(self, obj):
        return sum(item.sub_total() for item in obj.cartitem_set.all())
    total_price.short_description = "Total Price"
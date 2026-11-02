from django.contrib import admin
from .models import Customer, Channel, Service


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("is_active",)


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("is_active",)




@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    exclude = ("created_by",)

    list_display = (
        "customer",
        "channel",
        "service_type",
        "protocol",
        "public_ip",
        "port",
        "mode",
        "status",
        "created_at",
    )

    search_fields = (
        "customer__name",
        "channel__name",
        "public_ip",
    )

    list_filter = (
        "service_type",
        "protocol",
        "mode",
        "status",
    )

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
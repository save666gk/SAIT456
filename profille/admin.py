from django.contrib import admin
from .models import License, Purchase, Update, Payment, Product

@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('license_key', 'user', 'issue_date', 'expiration_date', 'created_at', 'updated_at')
    search_fields = ('license_key', 'user__username')
    list_filter = ('issue_date', 'expiration_date')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'purchase_date', 'amount', 'created_at', 'updated_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('purchase_date',)

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('version', 'product', 'release_date', 'created_at', 'updated_at')
    search_fields = ('version', 'product__name')
    list_filter = ('release_date',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'payment_date', 'status', 'created_at', 'updated_at')
    search_fields = ('user__username',)
    list_filter = ('payment_date', 'status')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'name', 'category', 'price', 'is_new', 'is_promo', 'promo_price']
    list_filter = ['category', 'is_new', 'is_promo']
    search_fields = ['name', 'description']
    list_editable = ['price', 'is_new', 'is_promo', 'promo_price']
    list_per_page = 20

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:8px;"/>', obj.image.url)
        return "📷 Pas d'image"
    image_preview.short_description = "Image"


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'total_price']
    readonly_fields = ['created_at']
    inlines = [OrderItemInline]
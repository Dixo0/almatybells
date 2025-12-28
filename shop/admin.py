from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product, Order, OrderItem

admin.site.site_header = "Панель управления Новогодним магазином"
admin.site.site_title = "Admin 2025"
admin.site.index_title = "Управление товарами и заказами"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['get_photo', 'name', 'category', 'price', 'stock', 'available', 'created']
    list_filter = ['available', 'created', 'category']
    list_editable = ['price', 'stock', 'available']
    search_fields = ['name', 'description']

    def get_photo(self, obj):
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url}" width="60" style="border-radius: 5px;">')
        return "Нет фото"

    get_photo.short_description = "Превью"


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'paid', 'created', 'total_cost']
    list_filter = ['paid', 'created']
    inlines = [OrderItemInline]

    def total_cost(self, obj):
        return f"{sum(item.price * item.quantity for item in obj.items.all())} тг."

    total_cost.short_description = "Сумма заказа"

from django.contrib import admin
from .models import Product, Catagory, Cart, Order, O_item, Wishlist
# Register your models here.


class Order_admin(admin.ModelAdmin):
    list_display = ('oid', 'name', 'email', 'amount',
                    'p_type', 'odate', 'status')
    list_filter = ('odate', 'status')
    search_fields = ('name', 'status',)
    list_editable = ('status',)


admin.site.register(Product)
admin.site.register(Catagory)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order, Order_admin)
admin.site.register(O_item)
